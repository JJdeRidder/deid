'''

Simple loading functions for datasets

   from deid.data import get_dataset

Copyright (c) 2017 Vanessa Sochat

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''


from deid.utils import get_installdir
from deid.logger import bot
import os


here = os.path.dirname(os.path.abspath(__file__))


def get_dataset(dataset=None):
    '''get_dataset will return some data provided by the application,
    based on a user-provided label. In the future, we can add https endpoints
    to retrieve online datasets.
    '''
    here = get_installdir()
    valid_datasets = {'dicom-cookies':'%s/data/dicom-cookies' %here}

    if dataset is not None:

        # In case the user gave an extension
        dataset = os.path.splitext(dataset)[0].lower()
        if dataset in valid_datasets:
            return valid_datasets[dataset]

    bot.info("Valid datasets include: %s" %(','.join(list(valid_datasets.keys()))))


def get_deid(tag=None, exit_on_fail=True, quiet=False):
    '''
    get deid is intended to retrieve the full path of a deid file provided with
    the software, based on a tag. For example, under deid/data if a file is called
    "deid.dicom", the tag would be "dicom". 

    Parameters
    ==========
    tag: the text that comes after deid to indicate the tag of the file in deid/data
    exit_on_fail: if None is an acceptable return value, this should be set to False
                  (default is True).
    quiet: Default False. If None is acceptable, quiet can be set to True

    '''
    # If it's a path, return full path
    if os.path.exists(tag):
        return os.path.abspath(tag)

    if tag is None:
        tag = "dicom"

    deid = "%s/deid.%s" %(here,tag)
    if not os.path.exists(deid):
        if quiet is False:
            bot.error("Cannot find %s" %(deid))
        if exit_on_fail is True:
            sys.exit(1)
        else:
            return None

    return "%s/deid.%s" %(here,tag)
