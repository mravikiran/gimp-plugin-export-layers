#-------------------------------------------------------------------------------
#
# This file is part of Export Layers.
#
# Copyright (C) 2013, 2014 khalim19 <khalim19@gmail.com>
# 
# Export Layers is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Export Layers is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with Export Layers.  If not, see <http://www.gnu.org/licenses/>.
#
#-------------------------------------------------------------------------------

#===============================================================================

import os

#===============================================================================

def test_export_layers(layer_exporter, main_settings):
  file_formats = ['raw', 'xcf', 'pix', 'matte', 'mask', 'alpha', 'als', 'fli', 'flc',
                  'xcf.bz2', 'xcfbz2', 'c', 'h', 'xhtml', 'dds', 'dcm', 'dicom', 'eps',
                  'fit', 'fits', 'gif', 'gbr', 'gih', 'pat', 'xcf.gz', 'xcfgz',
                  'html', 'htm', 'jpg', 'jpeg', 'jpe', 'cel', 'ico', 'mng', 'ora', 'pbm',
                  'pgm', 'psd', 'png', 'pnm', 'pdf', 'ps', 'ppm', 'sgi', 'rgb', 'rgba',
                  'bw', 'icon', 'im1', 'im8', 'im24', 'im32', 'rs', 'ras', 'tga', 'tif',
                  'tiff', 'bmp', 'xbm', 'bitmap', 'xpm', 'xwd', 'pcx', 'pcc']
  
  orig_output_directory = main_settings['output_directory'].value
  
  for file_format in file_formats:
    main_settings['file_format'].value = file_format
    main_settings['output_directory'].value = os.path.join(orig_output_directory, file_format)
    layer_exporter.export_layers()