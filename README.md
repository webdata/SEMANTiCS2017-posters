# SEMANTiCS2017-posters

This repository includes all accepted papers at the P&D track at [SEMANTiCS 2017](https://2017.semantics.cc/).

Camera ready papers are published in the [Research Articles in Simplified HTML (RASH)](https://www.google.com/url?q=https://github.com/essepuntato/rash&sa=D&ust=1502895361031000&usg=AFQjCNHaFU8umSWex0T8nAAKyb_Oe8Fpig) format, which allows one to easily prepare a scientific paper in HTML. It is composed by a few of the available HTML tags. In addition, it supports RDF annotations by means of Turtle, JSON-LD, RDF/XML, and RDFa. 

## How to produce HTML (RASH) papers

See the [SEMANTiCS HTML Submission Guideline](https://docs.google.com/document/d/1HcuDH8hPDV9Ye_VRKyfduXdVkfV6NAqx_fSO9_09O0Y/pub).

## How to process RASH to generate a Javascript-free HTML5 (for CEUR publication)

1. Save file as pure HTML

We use Firefox and its Web developer Toolbar.

* Open the HTML file and select View Source/View Generated Source
* Save the result 
* Remove the unnecessary final footer (it does not provide any functionality now), that is:

```
<footer class="footer hidden-print cgen" data-rash-original-content=""><p><span>Words: 760</span><span>Figures: 0</span><span>Tables: 0</span><span>Formulas: 0</span><span>Listings: 0</span></p><div class="btn-group dropup"><button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown" aria-expanded="false" onclick="$(this).toggleCSS()">Layout: <span id="layoutselection">Web-based</span><span class="caret"></span></button><ul class="dropdown-menu" role="menu"><li><a href="#rash_web_based_layout" onclick="$(this).changeCSS('#rash_web_based_layout')">Web-based</a></li><li><a href="#rash_lncs_layout" onclick="$(this).changeCSS('#rash_lncs_layout')">Springer LNCS</a></li></ul></div><p></p></footer>
```

2. Adapt the text to pass the HTML 5 validation: https://validator.w3.org 

*  Remove all references to javascript. That is, remove:

```
<script src="js/jquery.min.js"> </script>
<script src="js/bootstrap.min.js"> </script>
<script src="js/rash.js"> </script>
<script id="" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS-MML_HTMLorMML"> </script>
```
* Add to the beginning the HTML declaration:

```
<!DOCTYPE HTML>
```

* Fix the footnotes: The links of footnotes are nested, which is not accepted. One can find something like:

```
<a href="#ftn0"><sup class="fn cgen" data-rash-original-content=" "><a name="fn_pointer_ftn0" title="Footnote 1: https://www.big-data-europe.eu/">1</a></sup></a> 
```

This should be replaced with (note that the outter link is removed, the href property is included in the inner link and the name property is replaced by an id property):

```
<sup class="fn cgen" data-rash-original-content=" "><a href="#ftn1" id="fn_pointer_ftn1" title="Footnote 2: https://www.big-data-europe.eu/">2</a></sup>
```

3. Change roles with classes

There are validations errors regarding the doc-* roles. All the doc-* roles comes from the DPUB-ARIA specification: https://www.w3.org/TR/dpub-aria-1.0/, which would be soon a candidate recommendation and included in the validator. 

Until then, one could do the following procedure to be safe of errors:

* In the HTML file, replace all occurrences of **role=** with **class=** in HTML tags (essentially, *section* and *li* tags)


* In the *css/rash.css file*, replace all occurrences of **role=** with **class=** 





