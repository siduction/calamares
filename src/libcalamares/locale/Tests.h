/* === This file is part of Calamares - <https://github.com/calamares> ===
 *
 *   Copyright 2019, Adriaan de Groot <groot@kde.org>
 *
 *   Calamares is free software: you can redistribute it and/or modify
 *   it under the terms of the GNU General Public License as published by
 *   the Free Software Foundation, either version 3 of the License, or
 *   (at your option) any later version.
 *
 *   Calamares is distributed in the hope that it will be useful,
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 *   GNU General Public License for more details.
 *
 *   You should have received a copy of the GNU General Public License
 *   along with Calamares. If not, see <http://www.gnu.org/licenses/>.
 */

#ifndef LIBCALAMARES_LOCALE_TESTS_H
#define LIBCALAMARES_LOCALE_TESTS_H

#include <QObject>

class LocaleTests : public QObject
{
    Q_OBJECT
public:
    LocaleTests();
    ~LocaleTests() override;

private Q_SLOTS:
    void initTestCase();

    void testLanguageModelCount();
    void testEsperanto();
    void testTranslatableLanguages();
    void testTranslatableConfig1();
    void testTranslatableConfig2();
};

#endif
