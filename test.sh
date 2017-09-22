#bin/sh

# you need wkhtmltopdf with qt patches

ls papers_final | while read -r a;
do
	if [ ! -e "papers_final/$a/$a.pdf" ]; then
		echo $a
	fi
done
