
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
import QtQuick.Controls 1.2
import QtQuick.Controls.Styles 1.2
import ArcGIS.Runtime 10.26
import QtPositioning 5.3

ApplicationWindow {
    id: appWindow
    width: 800
    height: 600
    title: "App Tracks"

    property variant definitionAttribute: "Walking";
    property bool canCapture: false;
    property string featuresUrl: "http://services.arcgis.com/Wl7Y1m92PbjtJs5n/arcgis/rest/services/NothingInIt/FeatureServer";
    property string gdbPath: "~/ArcGIS/Runtime/Data/Test/myPoints.geodatabase"
    property double scaleFactor: System.displayScaleFactor
    property int fontSize: 15 * scaleFactor
    property bool isOnline: true;

    Map {
        id: mainMap
        anchors.fill: parent

        focus: true

        onStatusChanged: {
                    if (status === Enums.MapStatusReady) {
                        ps.active = true;
                        statusText.text = "Getting service info";
                        serviceInfoTask.fetchFeatureServiceInfo();
                    }
        }

        ArcGISTiledMapServiceLayer {
            url: "http://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer"
        }

        GeodatabaseFeatureServiceTable {
                    id: featureServiceTable
                    url: featuresUrl + "/0";
                }

        GeodatabaseFeatureTable {
            id: local
            geodatabase: gdb.valid ? gdb : null
            featureServiceLayerId: 0
        }

        GeodatabaseSyncStatusInfo {
            id: syncStatusInfo
        }

        ServiceInfoTask {
                id: serviceInfoTask
                url: featuresUrl

                onFeatureServiceInfoStatusChanged: {

                    if (featureServiceInfoStatus === Enums.FeatureServiceInfoStatusCompleted) {
                        statusText.text = "Service info received. Tap on the Generate Geodatabase Button";

                        generateButton.enabled = true;
                    } else if (featureServiceInfoStatus === Enums.FeatureServiceInfoStatusErrored) {
                        statusText.text = "Error:" + errorString;
                        generateButton.enabled = false;
                        cancelButton.text = "Start Over";
                    }
                }
            }

        FeatureLayer {
            id: featureLayer
            featureTable: isOnline ? featureServiceTable: local
            definitionExpression: "ONE = '"+definitionAttribute+"'"

            function addTracked(feature)
            {
                if (featureTable.featureTableStatus === Enums.FeatureTableStatusInitialized) {
                    console.log(featureTable.addFeature(feature));
                    featureServiceTable.applyFeatureEdits();
                }
            }
        }

        Point {
            id: pointToAdd
            x: 100
            y: 100
            spatialReference: SpatialReference
            {
                wkid:3857
            }
        }

        positionDisplay {
            id: pd
            zoomScale: 17
            mode: Enums.AutoPanModeCompass;
            positionSource: PositionSource {
                id: ps
            }
            onMapPointChanged: {
                if (pd.geoPoint.x != 0 && pd.geoPoint.y != 0 && canCapture)
                {
                    pointToAdd.setXY(pd.mapPoint.x, pd.mapPoint.y);
                    var featureToAdd = ArcGISRuntime.createObject("Feature");
                    featureToAdd.geometry = pointToAdd;
                    featureToAdd.setAttributeValue("One", definitionAttribute);
                    console.log(featureToAdd.toString())
                    featureLayer.addTracked(featureToAdd);
                }
            }
        }

Rectangle {
    //id: optionsRectangle
    anchors {
        fill: controlsColumn
        margins: 10 * scaleFactor
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
                id: controlsColumn
                anchors {
                    left: parent.left
                    top: parent.top
                    margins: 20 * scaleFactor
                }
                spacing: 4

                Button {
                    id: generateButton
                    text: "Generate Geodatabase"
                    enabled: false
                    style: ButtonStyle {
                        label: Text {
                            text: control.text
                            color: control.enabled ? "black" : "grey"
                            horizontalAlignment: Text.AlignHCenter
                        }
                    }

                    onClicked: {
                        generateGeodatabaseParameters.initialize(serviceInfoTask.featureServiceInfo);
                        generateGeodatabaseParameters.extent = mainMap.extent;
                        generateGeodatabaseParameters.returnAttachments = false;
                        statusText.text = "Starting generate geodatabase task";
                        geodatabaseSyncTask.generateGeodatabase(generateGeodatabaseParameters, gdbPath);
                    }
                }

                Button {
                    id: syncButton
                    text: "Sync"
                    width: generateButton.width
                    enabled: false
                    style: generateButton.style

                    onClicked: {
                        enabled = false;
                        geodatabaseSyncTask.syncGeodatabase(gdb.syncGeodatabaseParameters, gdb);
                        statusText.text = "Starting sync task";
                    }
                }
                TextEdit {
                    id: attributeUpdateArea
                    text: "Update Me"
                    width: generateButton.width
                    enabled: true
                    onTextChanged: {
                        updateText.enabled = true
                    }
                }
                Button {
                    id: updateText
                    text: "Update Attribute"
                    width: generateButton.width
                    enabled: true
                    style: generateButton.style

                    onClicked: {
                        definitionAttribute = attributeUpdateArea.text;
                        updateText.enabled = false;
                    }
                }
                }
            }



        Geodatabase {
            id: gdb
            path: geodatabaseSyncTask.geodatabasePath

            onValidChanged: {
                if (valid) {
                    var gdbtables = gdb.geodatabaseFeatureTables;
                    for(var i in gdbtables) {
                        console.log (gdbtables[i].featureServiceLayerName);
                    }
                }
            }
        }

        GeodatabaseSyncTask {
            id: geodatabaseSyncTask
            url: featuresUrl

            onGenerateStatusChanged: {
                if (generateStatus === Enums.GenerateStatusCompleted) {
                    canCapture = true;
                    statusText.text = geodatabasePath;
                    generateButton.enabled = false;
                    syncButton.enabled = true;
                    isOnline = true;

                }
                else if (generateStatus === GeodatabaseSyncTask.GenerateError) {
                    statusText.text = "Error: " + generateGeodatabaseError.message + " Code= "  + generateGeodatabaseError.code.toString() + " "  + generateGeodatabaseError.details;

                }
            }

            onGeodatabaseSyncStatusInfoChanged: {
                if (geodatabaseSyncStatusInfo.status === Enums.GeodatabaseStatusUploadingDelta) {
                    var deltaProgress = geodatabaseSyncStatusInfo.deltaUploadProgress/1000;
                    var deltaSize = geodatabaseSyncStatusInfo.deltaSize/1000;
                    statusText.text = geodatabaseSyncStatusInfo.statusString + " " + String(deltaProgress) + " of " + String(deltaSize) + " KBs...";
                } else
                    statusText.text = geodatabaseSyncStatusInfo.statusString + "...";
                if (geodatabaseSyncStatusInfo.status !== GeodatabaseSyncStatusInfo.Cancelled)
                    //cancelButton.enabled = true;
                syncStatusInfo.json = geodatabaseSyncStatusInfo.json;
            }

            onSyncStatusChanged: {
                featureServiceTable.refreshFeatures();
                if (syncStatus === Enums.SyncStatusCompleted) {
                    //cancelButton.enabled = false;
                    syncButton.enabled = false;
                    statusText.text = "Sync completed. You may continue editing the features.";
                    //switchToggle.enabled = true;
                    canCapture = false;
                    generateButton.enabled = true;
                }
                if (syncStatus === Enums.SyncStatusErrored)
                    statusText.text = "Error: " + syncGeodatabaseError.message + " Code= "  + syncGeodatabaseError.code.toString() + " "  + syncGeodatabaseError.details;
            }
        }

        GenerateGeodatabaseParameters {
            id: generateGeodatabaseParameters
        }

        Rectangle {
            id: textStatusRectangle
            anchors {
                fill: statusText
                margins: -10 * scaleFactor
            }
            visible: statusText.text.length > 0
            color: "lightgrey"
            radius: 5
            border.color: "black"
            opacity: 0.77
        }

        Text {
            id: statusText
            anchors {
                left: parent.left
                right: parent.right
                bottom: parent.bottom
                margins: 20 * scaleFactor
            }
            wrapMode: Text.WordWrap
            color: "black"
        }

        Rectangle {
            anchors.fill: parent
            color: "transparent"
            border {
                width: 0.5 * scaleFactor
                color: "black"
            }
        }

        }
