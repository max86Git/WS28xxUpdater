# WS28xx to Weathercloud Data Uploader

This script reads weather data from a **currdat.lst** file, formats it, and sends it to the Weathercloud service through their API.


## Prerequisites

- Python 3.x
- **requests** module (can be installed with **pip**)

## Usage

1.  Clone this repository or download the `weathercloud_uploader.py` file.
2.  Open the `weathercloud_uploader.py` file in a text editor.
3.  Set your Weathercloud ID and API key in the `weathercloudID` and `weathercloudAPIKey` variables, respectively.
4.  Set the path to your `currdat.lst` file in the `currdat_path` variable.
5.  Set the update interval (in seconds) in the `update_interval` variable.
6.  Save the changes and run the script using `python weathercloud_uploader.py` in a terminal or command prompt.

The script will run continuously, sending weather data to Weathercloud every `update_interval` seconds.

## Notes

-   The script reads data from `currdat.lst` assuming it's formatted according to the Heavy Weather Pro software from LaCrosse WS28xx weather station specifications.
-   The script uses the `datetime` and `requests` modules, which are part of the Python standard library and `requests` needs to be installed beforehand.
-   The script sends the data in the metric unit system (Celsius, meters per second, millimeters, hectopascals). It can be easily modified to use imperial units.

## License

Feel free to take a look at the source and adapt as you please. This source is licensed as follows:

[![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-sa/4.0/)

WS28xx to Weathercloud Data Uploader is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).