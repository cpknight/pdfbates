#!/usr/bin/env python3
# ----------------------------------------------------------------------------
# pdfbates.py - Very Simple PDF Page Counter for python3
# ----------------------------------------------------------------------------
# Note: This code is subject to a BSD 2-clause licence that appears below.
# ----------------------------------------------------------------------------

import sys
from PyPDF2 import PdfFileReader

if (len(sys.argv) < 2):
  print("Usage: " + sys.argv[0] + " [PDF filename]")
  print("   eg. " + sys.argv[0] + " DOC00001.pdf")
  sys.exit(1)

originalPDF    = PdfFileReader(open(sys.argv[1], "rb"))
numberOfPages  = originalPDF.getNumPages()

print(numberOfPages)

# ----------------------------------------------------------------------------
# Copyright (c) 2016, Christopher P. Knight. All rights reserved.
#
# Redistribution  and  use  in  source  and  binary  forms,  with or  without 
# modification, are permitted provided that the following conditions are met:
# 
# 1. Redistributions of  source  code must retain the above copyright notice, 
#    this list of conditions and the following disclaimer.
# 
# 2. Redistributions  in  binary  form  must  reproduce  the  above copyright 
#    notice,  this list  of  conditions  and  the following disclaimer in the 
#    documentation and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND  ANY  EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
# IMPLIED  WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
# ARE  DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE 
# LIABLE  FOR  ANY DIRECT,  INDIRECT,   INCIDENTAL,  SPECIAL,  EXEMPLARY,  OR 
# CONSEQUENTIAL  DAMAGES  (INCLUDING,  BUT  NOT  LIMITED  TO, PROCUREMENT  OF 
# SUBSTITUTE  GOODS OR SERVICES;  LOSS OF USE, DATA, OR PROFITS;  OR BUSINESS 
# INTERRUPTION) HOWEVER  CAUSED  AND ON ANY  THEORY OF LIABILITY,  WHETHER IN 
# CONTRACT,  STRICT  LIABILITY,  OR TORT  (INCLUDING NEGLIGENCE OR OTHERWISE) 
# ARISING  IN ANY WAY  OUT OF THE USE  OF THIS  SOFTWARE,  EVEN IF ADVISED OF 
# THE POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------
#                                                                          eof