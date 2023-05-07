-- User

INSERT INTO `user` (`username`, `pwd`, `fname`, `lname`, `lastlogin`, `nickname`) VALUES
('ab123', 'pwd1234', 'Lakshana', 'Kolur', '2023-02-17', 'Lakur'),
('abr9982', 'pwd2234', 'Alison', 'Reed', NULL, 'Lakur'),
('ap2963', 'pwd3234', 'Agnes', 'Park', '2023-03-14', NULL),
('gs3687', NULL, 'Genesis', 'Smothers', '2023-01-11', 'Genrs'),
('hp2229', 'pwd5234', 'Hansaem', 'Park', NULL, NULL),
('kp2690', 'pwd6234', 'Kaiyu', 'Pei', NULL, 'Kaipe'),
('mm13064', NULL, 'Makendy', 'Midouin', '2020-02-17', 'Makmi'),
('pa1363', 'pwd8234', 'Prabhav', 'Arora', '2021-05-16', 'Praar'),
('ql2326', 'pwd9234', 'Mike', 'Liu', '2020-01-10', 'Mikli'),
('sh4480', 'pwd1334', 'Shihui', 'Huang', '2023-02-18', 'Shihu'),
('sk9223', NULL, 'Srija', 'Konjarla', NULL, NULL),
('ss9040', 'pwd1534', 'Sonia', 'Susanto', '2023-08-17', 'Sonsu'),
('tm3566', 'pwd1634', 'Thomas', 'Maher', '2021-01-16', 'Thoma'),
('tm4033', 'pwd1734', 'Tony', 'Maricic', '2022-11-17', 'Tonma'),
('wc1609', 'pwd1834', 'Wanzhao', 'Cheng', '1999-09-01', 'Wanch'),
('wc2276', 'pwd1934', 'Wei', 'Chen', NULL, 'Weich'),
('wx682', 'pwd1644', 'Wei', 'Xia', '2021-10-15', 'Weixi'),
('xj2096', 'pwd1654', 'Alice', 'Jiang', '1998-09-15', 'Aliji'),
('zf2155', 'pwd1664', 'Zayyan', 'Farooqi', NULL, 'Zayfa'),
('zs1282', 'pwd1674', 'Claudia', 'Shao', '2020-07-24', 'Clash');

-- Song

INSERT INTO `song` (`songID`, `title`, `releaseDate`, `songURL`) VALUES
('S1111', 'Lost On You', '2018-02-17', 'Song1111_url'),
('S1112', 'Ghost', '2022-11-10', 'Song1112_url'),
('S1113', 'Bam Bam', '2017-02-18', 'Song1113_url'),
('S1114', 'Love Story', NULL, NULL),
('S1115', 'Suzume', '2022-06-01', 'Song1115_url'),
('S1116', 'Bad Boy', '2019-11-17', NULL),
('S1117', 'Belladona', NULL, 'Song1117_url'),
('S1119', 'Try', '2001-01-11', 'Song1119_url'),
('S1121', 'Fields of Gold', '1988-07-12', 'Song1121_url'),
('S1122', 'Galway Girl', '2015-10-10', 'Song1122_url'),
('S1123', 'Nancy Mulligan', '2016-11-10', NULL),
('S1124', 'I See Fire', '2018-02-17', 'Song1124_url'),
('S1125', 'Drunken Sailor', '2022-03-11', 'Song1125_url'),
('S1126', 'Viva La Vida', '2005-02-18', 'Song1126_url'),
('S1127', 'Hymn For The Weekend', '2010-11-17', 'Song1127_url');

-- Artist

INSERT INTO `artist` (`artistID`, `fname`, `lname`, `artistBio`, `artistURL`) VALUES
('AR111', 'Ed', 'Sheeran', 'SweetHeart Music', 'AR111_url'),
('AR122', 'Ava', 'Max', 'Hip Hop Music', 'AR122_url'),
('AR133', 'Taylor', 'Swift', 'SweetHeart Music', 'AR133_url'),
('AR144', 'Indilla', 'Kaur', 'SweetHeart Music', 'AR144_url'),
('AR155', 'Coldplay', 'Band', 'Pop Music', 'AR155_url'),
('AR166', 'Radwimps', 'Band', 'Anime Music', 'AR166_url'),
('AR177', 'Malinda', 'Sules', 'Cover Music', 'AR177_url'),
('AR188', 'Celtic', 'Woman', 'Folk Music', 'AR188_url'),
('AR199', 'Camila', 'Cabello', 'SweetHeart Music', 'AR199_url'),
('AR211', 'LP', 'Solo', 'Melody Music', 'AR211_url'),
('AR222', 'Colby', 'Colbairt', 'Indie Music', 'AR222_url'),
('AR233', 'One', 'Republic', 'Pop Music', 'AR233_url'),
('AR244', 'Linkin', 'Park', 'Rap Music', 'AR244_url');

-- Album

INSERT INTO `album` (`albumID`) VALUES
('AL111'),
('AL122'),
('AL133'),
('AL144'),
('AL155'),
('AL166'),
('AL177'),
('AL188'),
('AL199'),
('AL211');

-- Friend

INSERT INTO `friend` (`user1`, `user2`, `acceptStatus`, `requestSentBy`, `createdAt`, `updatedAt`) VALUES
('ab123', 'wc2276', 'Accepted', 'ab123', '2022-12-31 23:59:59', '2023-01-31 23:59:59'),
('ab123', 'ap2963', 'Pending', 'ab123', '2021-11-07 22:00:00', '2021-11-07 22:00:00'),
('ab123', 'gs3687', 'Not accepted', 'ab123', '2022-12-31 23:59:59', '2023-01-31 23:59:59'),
('ap2963', 'gs3687', 'Pending', 'ap2963', '2022-11-11 22:00:00', '2022-11-11 22:00:00'),
('gs3687', 'zs1282', 'Accepted', 'gs3687', '2022-11-30 23:59:59', '2022-12-30 23:59:59'),
('hp2229', 'pa1363', 'Accepted', 'hp2229', '2023-01-31 23:59:59', '2023-02-11 23:59:59'),
('hp2229', 'ab123', 'Accepted', 'hp2229', '2023-01-31 23:58:58', '2023-01-31 23:59:59'),
('hp2229', 'zs1282', 'Accepted', 'hp2229', '2022-11-30 23:59:59', '2022-12-30 23:59:59'),
('tm3566', 'ab123', 'Accepted', 'tm3566', '2022-12-31 23:59:59', '2023-01-31 23:59:59'),
('tm3566', 'gs3687', 'Not accepted', 'tm3566', '2022-12-31 23:59:59', '2023-01-31 23:59:59'),
('tm3566', 'zs1282', 'Not accepted', 'tm3566', '2022-12-31 23:59:59', '2023-01-31 23:59:59');

-- Follows

INSERT INTO `follows` (`follower`, `follows`, `createdAt`) VALUES
('ab123', 'abr9982', '2022-12-31 23:59:59'),
('ab123', 'xj2096', '2021-11-07 22:00:00'),
('ab123', 'ss9040', '2023-01-31 23:59:59'),
('ap2963', 'wc1609', '2022-11-11 22:00:00'),
('gs3687', 'wc1609', '2022-12-30 23:59:59'),
('hp2229', 'pa1363', '2023-02-11 23:59:59'),
('hp2229', 'wx682', '2023-01-31 23:59:59'),
('hp2229', 'zs1282', '2022-12-30 23:59:59'),
('tm3566', 'wx682', '2023-01-31 23:59:59'),
('tm3566', 'sk9223', '2023-01-31 23:59:59'),
('tm3566', 'zf2155', '2023-01-31 23:59:59');

-- RateAlbum

INSERT INTO `rateAlbum` (`username`, `albumID`, `stars`) VALUES
('ab123', 'AL111', 3),
('ab123', 'AL177', 5),
('ab123', 'AL155', 5),
('ap2963', 'AL155', 1),
('gs3687', 'AL111', 2),
('hp2229', 'AL155', 2),
('hp2229', 'AL177', 4),
('hp2229', 'AL144', 3),
('tm3566', 'AL111', 4),
('tm3566', 'AL144', 5),
('tm3566', 'AL177', 1),
('gs3687', 'AL188', 2),
('ss9040', 'AL188', 2),
('pa1363', 'AL199', 4),
('hp2229', 'AL166', 3),
('hp2229', 'AL188', 4),
('ss9040', 'AL199', 5),
('tm3566', 'AL166', 2);

-- ReviewAlbum

INSERT INTO `reviewAlbum` (`username`, `albumID`, `reviewText`, `reviewDate`) VALUES
('ab123', 'AL111', 'Good Album', '2023-02-17'),
('ab123', 'AL177', 'Great songs in this album', '2023-01-17'),
('ab123', 'AL155', 'Good Album', '2023-03-17'),
('ap2963', 'AL155', 'Excellent Music', '2023-01-11'),
('gs3687', 'AL111', 'Excellent Music', '2023-01-11'),
('hp2229', 'AL155', 'Very Nice', '2023-02-11'),
('hp2229', 'AL177', 'Good Album', '2023-03-11'),
('hp2229', 'AL144', 'Great songs in this album', '2022-02-17'),
('tm3566', 'AL111', 'Very Nice', '2022-01-17'),
('tm3566', 'AL144', 'Good Album', '2022-09-17'),
('tm3566', 'AL177', 'Excellent Music', '2022-11-17'),
('gs3687', 'AL188', 'Great songs in this album', '2022-10-17'),
('pa1363', 'AL188', 'Excellent Music', '2023-01-31'),
('pa1363', 'AL199', 'Good Album', '2022-11-17'),
('hp2229', 'AL166', 'Great songs in this album', '2022-10-17'),
('ss9040', 'AL188', 'Very Nice', '2022-12-17'),
('hp2229', 'AL199', 'Great songs in this album', '2022-07-17'),
('tm3566', 'AL166', 'Excellent Music', '2022-06-17');

-- RateSong

INSERT INTO `rateSong` (`username`, `songID`, `stars`, `ratingDate`) VALUES
('ab123', 'S1111', 3, '2023-02-17'),
('ab123', 'S1115', 5, '2023-02-17'),
('ab123', 'S1121', 5, '2023-02-17'),
('ap2963', 'S1115', 1, '2022-07-11'),
('gs3687', 'S1115', 2, '2022-07-17'),
('hp2229', 'S1121', 2, '2022-07-17'),
('hp2229', 'S1115', 4, '2022-07-20'),
('hp2229', 'S1122', 3, '2022-07-17'),
('tm3566', 'S1111', 4, '2022-11-12'),
('tm3566', 'S1121', 5, '2022-10-11'),
('tm3566', 'S1122', 1, '2022-11-17'),
('gs3687', 'S1122', 2, '2022-11-17'),
('ss9040', 'S1125', 2, '2022-02-11'),
('pa1363', 'S1121', 4, '2022-01-17'),
('hp2229', 'S1111', 3, '2023-01-17'),
('ss9040', 'S1115', 4, '2022-02-17'),
('pa1363', 'S1111', 5, '2023-01-11'),
('tm3566', 'S1125', 2, '2023-01-11');

-- ReviewSong

INSERT INTO `reviewSong` (`username`, `songID`, `reviewText`, `reviewDate`) VALUES
('ab123', 'S1111', 'Great Song', '2023-02-17'),
('ab123', 'S1115', 'Love this song', '2023-02-17'),
('ab123', 'S1121', 'What a voice', '2023-02-17'),
('ap2963', 'S1115', 'Love it', '2022-07-11'),
('gs3687', 'S1115', 'Love it', '2022-07-17'),
('hp2229', 'S1121', 'Love this song', '2022-07-17'),
('hp2229', 'S1115', 'What a voice', '2022-07-20'),
('hp2229', 'S1122', 'Great Song', '2022-07-17'),
('tm3566', 'S1111', 'Great Song', '2022-11-12'),
('tm3566', 'S1121', 'Love this song', '2022-10-11'),
('tm3566', 'S1122', 'Love it', '2022-11-17'),
('gs3687', 'S1122', 'What a voice', '2022-11-17'),
('ss9040', 'S1125', 'Great Song', '2022-02-11'),
('pa1363', 'S1121', 'What a voice', '2022-01-17'),
('hp2229', 'S1111', 'Love this song', '2023-01-17'),
('ss9040', 'S1115', 'What a voice', '2022-02-17'),
('pa1363', 'S1111', 'Love it', '2023-01-11'),
('tm3566', 'S1125', 'Love this song', '2023-01-11');

-- SongInAlbum

INSERT INTO `songInAlbum` (`albumID`, `songID`) VALUES
('AL111', 'S1111'),
('AL122', 'S1112'),
('AL133', 'S1121'),
('AL144', 'S1112'),
('AL155', 'S1111'),
('AL166', 'S1112'),
('AL177', 'S1121'),
('AL188', 'S1112'),
('AL199', 'S1111'),
('AL211', 'S1112'),
('AL111', 'S1122'),
('AL122', 'S1126'),
('AL133', 'S1122'),
('AL144', 'S1126'),
('AL155', 'S1122'),
('AL166', 'S1126'),
('AL177', 'S1122'),
('AL188', 'S1126'),
('AL199', 'S1122'),
('AL211', 'S1126');

-- SongGenre

INSERT INTO `songGenre` (`songID`, `genre`) VALUES
('S1111', 'Jazz'),
('S1112', 'Pop'),
('S1113', 'Anime'),
('S1114', 'Rap'),
('S1115', 'Blues'),
('S1116', 'Rap'),
('S1117', 'Blues'),
('S1119', 'Jazz'),
('S1121', 'Pop'),
('S1122', 'Anime'),
('S1123', 'Jazz'),
('S1124', 'Blues'),
('S1125', 'Pop'),
('S1126', 'Anime'),
('S1127', 'Rap');

-- ArtistPerformsSong

INSERT INTO `artistPerformsSong` (`artistID`, `songID`) VALUES
('AR111', 'S1111'),
('AR211', 'S1112'),
('AR222', 'S1125'),
('AR233', 'S1112'),
('AR233', 'S1114'),
('AR155', 'S1112'),
('AR155', 'S1121'),
('AR166', 'S1112'),
('AR233', 'S1113'),
('AR188', 'S1112'),
('AR188', 'S1122'),
('AR188', 'S1126'),
('AR122', 'S1127'),
('AR122', 'S1126'),
('AR122', 'S1122'),
('AR222', 'S1124'),
('AR199', 'S1124'),
('AR199', 'S1127'),
('AR222', 'S1123'),
('AR211', 'S1126');

-- UserFanOfArtist

INSERT INTO `userFanOfArtist` (`username`, `artistID`) VALUES
('ab123', 'AR111'),
('tm3566', 'AR211'),
('gs3687', 'AR222'),
('ss9040', 'AR233'),
('pa1363', 'AR233'),
('ss9040', 'AR155'),
('pa1363', 'AR155'),
('ab123', 'AR166'),
('mm13064', 'AR233'),
('gs3687', 'AR188'),
('pa1363', 'AR188'),
('tm3566', 'AR188'),
('ab123', 'AR122'),
('hp2229', 'AR111'),
('hp2229', 'AR122'),
('hp2229', 'AR222'),
('ss9040', 'AR199'),
('tm3566', 'AR199'),
('mm13064', 'AR222'),
('gs3687', 'AR211');