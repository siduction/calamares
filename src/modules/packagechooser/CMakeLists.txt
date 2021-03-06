find_package( Qt5 COMPONENTS Core Gui Widgets REQUIRED )
set( _extra_libraries "" )
set( _extra_src "" )

### OPTIONAL AppData XML support in PackageModel
#
#
option( WITH_APPDATA "Support appdata: items in PackageChooser (requires QtXml)" ON )
if ( WITH_APPDATA )
    find_package(Qt5 COMPONENTS Xml)
    if ( Qt5Xml_FOUND )
        add_definitions( -DHAVE_XML )
        list( APPEND _extra_libraries Qt5::Xml )
        list( APPEND _extra_src ItemAppData.cpp )
    endif()
endif()

### OPTIONAL AppStream support in PackageModel
#
#
option( WITH_APPSTREAM "Support appstream: items in PackageChooser (requires libappstream-qt)" ON )
if ( WITH_APPSTREAM )
    find_package(AppStreamQt)
    set_package_properties(
        AppStreamQt PROPERTIES
        DESCRIPTION "Support for AppStream (cache) data"
        URL "https://github.com/ximion/appstream"
        PURPOSE "AppStream provides package data"
        TYPE OPTIONAL
    )
    if ( AppStreamQt_FOUND )
        add_definitions( -DHAVE_APPSTREAM )
        list( APPEND _extra_libraries AppStreamQt )
        list( APPEND _extra_src ItemAppStream.cpp )
    endif()
endif()

calamares_add_plugin( packagechooser
    TYPE viewmodule
    EXPORT_MACRO PLUGINDLLEXPORT_PRO
    SOURCES
        PackageChooserPage.cpp
        PackageChooserViewStep.cpp
        PackageModel.cpp
        ${_extra_src}
    RESOURCES
        packagechooser.qrc
    UI
        page_package.ui
    LINK_PRIVATE_LIBRARIES
        calamaresui
        ${_extra_libraries}
    SHARED_LIB
)

if( ECM_FOUND AND BUILD_TESTING )
    ecm_add_test(
            Tests.cpp
        TEST_NAME
            packagechoosertest
        LINK_LIBRARIES
            ${CALAMARES_LIBRARIES}
            calamares_viewmodule_packagechooser
            Qt5::Core
            Qt5::Test
            Qt5::Gui
            ${_extra_libraries}
    )
    calamares_automoc( packagechoosertest)
endif()
