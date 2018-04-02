# Pure RIS-to-CSV Converter #

This python script uses [regular expressions](https://en.wikipedia.org/wiki/Regular_expression) to convert [Research Information Systems]("https://en.wikipedia.org/wiki/RIS_(file_format)") (RIS) files to [Comma Separated Values](https://en.wikipedia.org/wiki/Comma-separated_values) (CSV) files. 

RIS files are one convenient way for researchers and data managers to store citations and send citations, but can be difficult to edit and use within the average workflow. The aim of this script is to make it easy to compare, edit, and view RIS data using the CSV file format, which has greater support in most established applications and workflows (such as [Microsoft Excel](https://products.office.com/en-us/excel), [LibreOffice Calc](https://www.libreoffice.org/discover/calc/), etc.). While some programs have implemented converters, they often make choices about formatting, inclusion/exclusion of data, etc. which may not be appropriate for all users. So this script is meant to fill the need for a _pure_ RIS-to-CSV converter that takes no such liberties. 

## Installation and Use ##

### For Those Without Programming Experience ##

If you don't want to deal with downloading/learning a programming language (or if you just want the program, not the algorithm), I have created both Windows and Unix executables that you can run like any other program on your computer. 

If you just want to download this program and use it, download this whole repository as a .zip file, unpack that zip file somewhere where you want it to live, then go into the `win_dist` folder if you are on Windows, or the `unix_dist` folder if you are on MacOS or Linux. You can then double click the `ris_converter` executable and use the program!


### For the techies ###

For those that want to dig a little deeper...
---------

Requirements:
* Python 3 (which can be downloaded and installed [here](https://www.python.org/downloads/))

Download this repository and make sure you have Python 3 installed. Using for favorite terminal emulator or Python IDE, run the script _ris_converter.py_ like so:
`python3 ris_converter.py`

Answer any prompts and the algorithm will create a new csv file for you at a specified location.

__Note__: Microsoft Excel can have trouble reading charactars that are not normal English characters (eg. ó, é, ö, etc.) that are encoded in the common Unicode (UTF-8) standard. [ScrapeHero](https://scrapehero.freshdesk.com/support/home) published [this article](https://scrapehero.freshdesk.com/support/solutions/articles/5000617795-how-to-open-csv-files-that-have-unicode-unprintable-or-weird-looking-characters-in-excel) describing one way to remedy this if you encouter such an issue.


