#bin/sh

# you need wkhtmltopdf with qt patches

ls papers_final | while read -r a;
do
	if [ ! -e "papers_final/$a/$a.pdf" ]; then
		echo $a
		../wkhtmltopdf -L 20mm -R 20mm -B 20mm -T 20mm papers_final/$a/index.html papers_final/$a/$a.pdf
	fi
done
