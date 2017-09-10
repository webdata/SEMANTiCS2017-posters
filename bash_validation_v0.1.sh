 #!/bin/bash
#BASH program to read an HTML file and a preffix


#READING the command line options -f = file name (path) -p the preffix
####This part is just for reading the options
HELP="\n $(basename "$0") [-h] -f file -p prefix -u RDFUnit -c tika \n\n
where:\n
	\t-h	\tshow this help message\n
	\t-f	\tsets the html file to be processed\n
	\t-p	\tsets the the prefix value\n
	\t-u	\tdefines the path of RDFUnit\n" 
#	\t-t	\tdefines the path of tika app (jar file)"\n


if [ "$1" = "-h" ] ; then
	echo -e $HELP
	exit 0
fi

while [[ $# -gt 1 ]]
do
key="$1"

case $key in
    -f|--file)
    FILE="$2"
    shift # past argument
    ;;
    -p|--prefix)
    PREFIX="$2"
    shift # past argument
    ;;  
    -u)
    RDFUNITPATH="$2"
    shift 
    ;;
    -t|--tika)
    TIKAPATH="$2"
    shift
    ;;
esac  
shift
done
##########end of reading options

#The complete path of the file
FILEPATH=$(readlink -f $FILE)
#How will be named the result from spotlight
SPOTLIGHTRESULT="$FILE-spotlight.ttl"
#How will be named the final result
HTMLRESULT="$FILEPATH-result.html"
#How will be named the output text file
#TIKAOUT="$FILEPATH-tika.txt"
PANDOCOUTPUT="$FILEPATH-pandoc.txt"
#LYNXOUTPUT="$FILEPATH-lynx.txt"
#XMLSTARTLET="$FILEPATH-xmlstartlet.txt"

echo "Extracting text from the HTML file ($FILE)"
#java -jar $TIKAPATH -t $FILEPATH > $TIKAOUT
#TEXTCONT=$(cat $TIKAOUT)
#TEXTCONT=$(java -jar $TIKAPATH -t $FILEPATH > "temp.txt") 
TEXTCONT=$(pandoc -f html -t plain $FILEPATH)
echo -e $TEXTCONT > $PANDOCOUTPUT
#TEXTCONT=$(lynx --dump $FILEPATH > $LYNXOUTPUT)
#TEXTCONT=$(xmlstarlet sel -t -v '/' $FILEPATH > $XMLSTARTLET)


echo "Running spotligh over the file $FILE with the prefix $PREFIX. The output file will be '$SPOTLIGHTRESULT'"
curl -X POST http://api.dbpedia-spotlight.org/rest/annotate --data "text=$TEXTCONT" --data "prefix=$PREFIX" --data "confidence=0.5" -H "Accept:text/turtle" > $SPOTLIGHTRESULT

##The complete path of the spotlight result file
FILEPATHSPOT=$(readlink -f $SPOTLIGHTRESULT)

##The output of RDFUnit is store, automatically, in the ../data/results/ folder. The name of the file is the complete path replacing the slash character for the underscore character
CONTENTOUTPUT=$(sed 's#/#\_#g' <<< $FILEPATHSPOT)

##I have some troubles running RDFUnit outside their main folder, then it was necessary to change to this directory
#RDFUnit="/home/julio/Downloads/RDFUnit-0.8.1/"
RDFUnit="$RDFUNITPATH/"
cd $RDFUnit

echo "Validating spotlight results ($SPOTLIGHTRESULT) with RDFUnit"

RDFUnitValidation=$(bin/rdfunit-dev -d $FILEPATHSPOT -s nif  -o html > /dev/null) 

echo "Attaching metadata (NIF data) to the original HTML file"

##checking if is aggregatedTestCaseResult or extendedTestCaseResult

file="data/results/$CONTENTOUTPUT.aggregatedTestCaseResult.ttl"

if [ -f "$file" ] && [ -s "$file" ] ; then
	AGGREGATERESULT=$file
else
	file="data/results/$CONTENTOUTPUT.extendedTestCaseResult.ttl"
	if [ -f "$file" ] && [ -s "$file" ] ; then
		AGGREGATERESULT=$file
	fi
fi

#Reading NIF data from the spotlight output

while read RES; do
	NIFCONT+="$RES\n"
done < $FILEPATHSPOT

#Attaching the NIF data to the original HTML
while read VAR; do
	if [ "$VAR" == "<head>" ]; then
		NEWF+="$VAR\n<script type='text/turtle'>\n$NIFCONT\n</script>\n"
	else
		NEWF+="$VAR\n"
	fi
done < $FILEPATH

#writing the HTML with the NIF data attached
echo -e $NEWF > $HTMLRESULT
echo "Process finish"
