
// Copyright 2015 ESRI
//
// All rights reserved under the copyright laws of the United States
// and applicable international laws, treaties, and conventions.
//
// You may freely redistribute and use this sample code, with or
// without modification, provided you include the original copyright
// notice and use restrictions.
//
// See the Sample code usage restrictions document for further information.
//

import QtQuick 2.3
import QtQuick.Controls 1.0
import QtQuick.Controls.Styles 1.2
import ArcGIS.Extras 1.0
import QtQuick 2.3
import QtQuick.Controls 1.2
import QtQuick.Controls.Styles 1.2
import ArcGIS.Runtime 10.26
import QtPositioning 5.3

ApplicationWindow {
    id: appWindow
    width: 800
    height: 600
    title: "Geocache Finder"

    property double scaleFactor: System.displayScaleFactor
    property bool canCapture: false;
    property int fontSize: 20
    property string distanceToPoint: "100"
    property Point myLocation

    Map {
        anchors.fill: parent

        focus: true

        onStatusChanged:  {
            if (status == Enums.MapStatusReady)
            {
                ps.active = true;
            }
        }

        ArcGISTiledMapServiceLayer {
            url: "http://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer"
        }

        SpatialReference {
            id: newRef
                wkid:3857
                                 }

        Point {
            id: pointProjected
            x: 0
            y: 0
            spatialReference: SpatialReference
            {
            wkid: 3857
            }
        }

        Point {
            id: pointToTrack
            x: -10
            y: 38
            spatialReference: SpatialReference
            {
                wkid:4326
            }
        }

    GraphicsLayer {
        id:graphicLayer

    Graphic {
        id: graphicPointToTrack
        geometry: pointProjected
        symbol: SimpleMarkerSymbol {
            style: Enums.SimpleMarkerSymbolStyleDiamond
            color: "steelblue"
            size: 35
        }
       }
    }

        positionDisplay {
            id: pd
            zoomScale: 17
            mode: Enums.AutoPanModeNavigation;
            positionSource: PositionSource {
                id: ps
            }
            onMapPointChanged: {
                myLocation = pd.mapPoint
                var distanceBetween = myLocation.distance(pointProjected);
                distanceToPoint = distanceBetween;
            }
        }

        Rectangle {
            //id: optionsRectangle
            anchors {
                fill: contorlColumn
                margins: .02 * scaleFactor
            }

            color: "lightgrey"
            radius: 5 * scaleFactor
            border.color: "black"
            opacity: 0.88

            MouseArea {
                anchors.fill: parent
                onClicked: (mouse.accepted = true)
            }
        }

    Column {
        id: contorlColumn
        anchors {
            leftMargin: 21
            topMargin: 21
            left: parent.left
            top: parent.top
            margins: 20 * scaleFactor
        }

        Text {
            id: text1
            text: qsTr("XCoordinate:   ")
            font.pixelSize: 14 * scaleFactor

            TextEdit {
                id: textEdit1
                anchors.left: text1.right
                width: 80
                height: 20
                text: qsTr("-75")
                font.pixelSize: 14 * scaleFactor

            onTextChanged: {
                pointToTrack.setXY(textEdit1.text, textEdit2.text)
                var tempPoint =pointToTrack.project(newRef)
                pointProjected.json = tempPoint.json
            }
            }
        }

        Text {
            id: text2
            text: qsTr("YCoordinate:   ")
            font.pixelSize: 14 * scaleFactor

            TextEdit {
                id: textEdit2
                anchors.left: text2.right
                width: 80
                height: 20
                text: qsTr("38")
                font.pixelSize: 14 * scaleFactor
            onTextChanged: {
                pointToTrack.setXY(textEdit1.text, textEdit2.text)
                var tempPoint =pointToTrack.project(newRef)
                pointProjected.json = tempPoint.json
            }
            }
        }

        Text {
            id: distanceLabel
            text: qsTr("Distance From Point:   " + distanceToPoint + " meters")
            font.pixelSize: 14 * scaleFactor

        }
        spacing:4
    }


}
}
