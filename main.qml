

/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/
import QtQuick 6.2
import QtQuick.Controls 6.2

ApplicationWindow {
    visible: true
    width: 640
    height: 480
    color: "#ffffff"
    title: "Home Assistant"

    Button {
        id: button
        x: 259
        y: 216
        text: qsTr("Say Something")
    }

    Label {
        id: label
        x: 8
        y: 270
        width: 624
        height: 202
        text: qsTr("Label")
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignBottom
        font.pointSize: 16
    }
}
