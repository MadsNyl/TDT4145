-- Saler for Trøndelag Teater
INSERT INTO Sal
VALUES 
(1, 'Hovedscenen'),
(2, 'Gamle Scene');

-- Teaterstykker
INSERT INTO TeaterStykke
VALUES 
(1, 'Størst av alt er kjærligheten', 'Jonas Corell Petersen', 2),
(2, 'Kongsemnene', 'Henrik Ibsen', 1);

-- Akter
INSERT INTO Akt
VALUES 
-- Akter for 'Størst av alt er kjærligheten'
(1, 1, 'Akt 1', 1),
-- Akter for 'Kongsemnene'
(2, 1, 'Akt 1', 2),
(3, 2, 'Akt 2', 2),
(4, 3, 'Akt 3', 2),
(5, 4, 'Akt 4', 2),
(6, 5, 'Akt 5', 2);

-- Start ansatte for 'Størst av alt er kjærligheten'
INSERT INTO Ansatt
VALUES 
-- Ansatte for 'Størst av alt er kjærligheten'
(1, 'Jonas Corell Petersen', 'jonas.petersen@trondheim.no', 'Fulltid'),
(2, 'David Gehrt', 'david.gehrt@trondheim.no', 'Fulltid'),
(3, 'Gaute Tønder', 'gaute.tønder@trondheim.no', 'Fulltid'),
(4, 'Magnus Mikaelsen', 'magnus.mikaelsen@trondheim.no', 'Fulltid'),
(5, 'Kristoffer Spender', 'kristoffer.spender@trondheim.no', 'Fulltid'),
-- Skuespillere for 'Størst av alt er kjærligheten'
(6, 'Sunniva Du Mond Nordal', 'sunniva.nordal@trondheim.no', 'Fulltid'),
(7, 'Jo Saberniak', 'jo.saberniak@trondheim.no', 'Fulltid'),
(8, 'Marte M. Steinholt', 'marte.steinholt@trondheim.no', 'Fulltid'),
(9, 'Tor Ivar Hagen', 'tor.hagen@trondheim.no', 'Fulltid'),
(10, 'Trond-Ove Skrødal', 'trond.skrødal@trondheim.no', 'Fulltid'),
(11, 'Natalie Grøndahl Tangen', 'natalie.tangen@trondheim.no', 'Fulltid'),
(12, 'Åsmund Flaten', 'åsmund.flaten@trondheim.no', 'Fulltid'),
-- Ansatte for 'Kongsemnene'
(13, 'Yury Butusov', 'yury.butusov@trondheim.no', 'Fulltid'),
(14, 'Aleksandr Shishkin-Hokusai', 'aleksandr.hokusai@trondheim.no', 'Fulltid'),
(15, 'Eivind Myren', 'eiving.myren@trondheim.no', 'Fulltid'),
(16, 'Mina Rype Stokke', 'mina.stokke@trondheim.no', 'Fulltid'),
-- Skuespillere for 'Kongsemnene'
(17, 'Arturo Scotti', 'arturo.scotti@trondheim.no', 'Fulltid'),
(18, 'Ingunn Beate Strige Øyen', 'ingunn.strige@trondheim.no', 'Fulltid'),
(19, 'Hans Petter Nilsen', 'hanspetter.nilsen@trondheim.no', 'Fulltid'),
(20, 'Madeleine Brandtzæg Nilsen', 'madeleine.nilsen@trondheim.no', 'Fulltid'),
(21, 'Synnøve Fossum Eriksen', 'synnove.eriksen@trondheim.no', 'Fulltid'),
(22, 'Emma Caroline Deichmann', 'emma.deichmann@trondheim.no', 'Fulltid'),
(23, 'Thomas Jensen Takyi', 'thomas.takyi@trondheim.no', 'Fulltid'),
(24, 'Per Bogstad Gulliksen', 'per.gulliksen@trondheim.no', 'Fulltid'),
(25, 'Isak Holmen Sørensen', 'isak.sorensen@trondheim.no', 'Fulltid'),
(26, 'Fabian Heidelberg Lunde', 'fabian.lunde@trondheim.no', 'Fulltid'),
(27, 'Emil Olafsson', 'emil.olafsson@trondheim.no', 'Fulltid'),
(28, 'Snorre Ryen Tøndel', 'snorre.tondel@trondheim.no', 'Fulltid');

-- Skuespillere
INSERT INTO Skuespiller (SkuespillerID)
VALUES
-- Skuespillere for 'Størst av alt er kjærligheten'
(6),
(7),
(8),
(9),
(10),
(11),
(12),
-- Skuespillere for 'Kongsemnene'
(17),
(18),
(19),
(20),
(21),
(22),
(23),
(24),
(25),
(26),
(27),
(28);


-- Teatermedarbeidere
INSERT INTO Teatermedarbeider (AnsattID, Rolle, TeaterStykke)
VALUES 
-- Teatermedarbeidere for 'Størst av alt er kjærligheten'
(1, 'Regi', 1),
(2, 'Scenografi og kostymer', 1),
(3, 'Musikalsk ansvarlig', 1),
(4, 'Lysdesign', 1),
(5, 'Dramaturg', 1),
-- Teatermedarbeidere for 'Kongsemnene'
(13, 'Regi og musikkutvelgelse', 2),
(14, 'Scenografi og kostymer', 2),
(15, 'Lysdesign', 2),
(16, 'Dramaturg', 2);


-- Roller
INSERT INTO Rolle
VALUES 
-- Roller for 'Størst av alt er kjærligheten'
(1, 'Spiller som seg selv'),
-- Roller for 'Kongsemnene'
(2, 'Haakon Haakonsønn'),
(3, 'Inga fra Vartjeg (Haakons mor)'),
(4, 'Skule jarl'),
(5, 'Fru Ragnhild (Skules hustru)'),
(6, 'Margrete (Skules datter)'),
(7, 'Sigrid (Skules søster)'),
(8, 'Ingebjørg'),
(9, 'Biskop Nikolas'),
(10, 'Per Bogstad Gulliksen'),
(11, 'Paal Flida'),
(12, 'Trønder'),
(13, 'Baard Bratte'),
(14, 'Jatgeir Skald'),
(15, 'Dagfinn Bonde'),
(16, 'Peter (pres og Ingebjørgs sønn)'),
(17, 'Guttorm Ingesson'),
(18, 'Gregorius Jonsson');

-- Mapping mellom roller og skuespillere
INSERT INTO SpillerSom
VALUES 
-- 'Størst av alt er kjærligheten'
(1, 6),
(1, 7),
(1, 8),
(1, 9),
(1, 10),
(1, 11),
(1, 12);

-- Mapping mellom akt og roller
INSERT INTO HarRoller (Akt, Rolle)
VALUES
-- 'Størst av alt er kjærligheten'
(1, 1),
-- 'Kongsemnene'
(2, 2),
(3, 2),
(4, 2),
(5, 2),
(6, 2),
(2, 15),
(3, 15),
(4, 15),
(5, 15),
(6, 15),
(5, 14),
(2, 7),
(3, 7),
(6, 7),
(5, 8),
(2, 17),
(2, 4),
(3, 4),
(4, 4),
(5, 4),
(6, 4),
(2, 3),
(4, 3),
(2, 11),
(3, 11),
(4, 11),
(5, 11),
(6, 11),
(2, 5),
(6, 5),
(2, 18),
(3, 18),
(4, 18),
(5, 18),
(6, 18),
(2, 6),
(3, 6),
(4, 6),
(5, 6),
(6, 6),
(2, 9),
(3, 9),
(4, 9),
(4, 16),
(5, 16),
(6, 16);



-- Forestillinger
INSERT INTO Forestilling
VALUES
-- Forestillinger for 'Størst av alt er kjærligheten'
(1, '2024-02-03 18:30:00', 1),
(2, '2024-02-06 18:30:00', 1),
(3, '2024-02-07 18:30:00', 1),
(4, '2024-02-12 18:30:00', 1),
(5, '2024-02-13 18:30:00', 1),
(6, '2024-02-14 18:30:00', 1),
-- Forestillinger for 'Kongsemnene'
(7, '2024-02-01 19:00:00', 2),
(8, '2024-02-02 19:00:00', 2),
(9, '2024-02-03 19:00:00', 2),
(10, '2024-02-05 19:00:00', 2),
(11, '2024-02-06 19:00:00', 2);


-- Standard Kundeprofil
INSERT INTO Kundeprofil
VALUES (
    1, 
    'Standard', 
    '12345678', 
    'Trondheimsgate 29'
);

-- Kundegrupper
INSERT INTO Kundegruppe
VALUES 
(1, 'Ordinær'),
(2, 'Honnør'),
(3, 'Student'),
(4, 'Gruppe 10'),
(5, 'Gruppe honnør 10'),
(6, 'Barn');


-- Billettpriser
INSERT INTO BillettPris
(BilettPrisID, Pris, Kundegruppe, TeaterStykke)
VALUES
-- Billettpriser for 'Størst av alt er kjærligheten'
(1, 350, 1, 1),
(2, 300, 2, 1),
(3, 220, 3, 1),
(4, 320, 4, 1),
(5, 270, 5, 1),
(6, 220, 6, 1),
-- Billettpriser for 'Kongsemnene'
(7, 450, 1, 2),
(8, 380, 2, 2),
(9, 280, 3, 2),
(10, 420, 4, 2),
(11, 360, 5, 2);