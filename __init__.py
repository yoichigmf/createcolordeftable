# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CreateColorDefTable
                                 A QGIS plugin
 Create color define table file from qml style file
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2024-07-04
        copyright            : (C) 2024 by Yoichi Kayama
        email                : yoichi.kayama@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load CreateColorDefTable class from file CreateColorDefTable.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .CreateColorDefTable import CreateColorDefTable
    return CreateColorDefTable(iface)
