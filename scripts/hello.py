#!/usr/bin/env python3
from datetime import datetime
import dev_aberto
import gettext
from babel.dates import format_date, format_datetime, format_time

gettext.install('cli', localedir='locale') 


if __name__ == '__main__':
    date, name = dev_aberto.hello()
    date_obj  = datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")
    print(_('Last commit made in:'), format_datetime(date_obj), _(' by'), name)
