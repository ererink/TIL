SELECT * 
FROM playlist_track AS 'A'
ORDER BY PlaylistId DESC
LIMIT 5;

SELECT * 
FROM tracks AS 'B'
ORDER BY TrackId
LIMIT 5;

SELECT PlaylistId, Name
FROM playlist_track INNER JOIN tracks
    ON playlist_track.TrackId = tracks.TrackId
ORDER BY PlaylistId DESC
LIMIT 10;

SELECT PlaylistId, Name
FROM playlist_track INNER JOIN tracks
    ON playlist_track.TrackId = tracks.TrackId
WHERE PlaylistId = '10'
ORDER BY Name DESC
LIMIT 5;

SELECT *
FROM tracks LEFT OUTER JOIN artists
    ON tracks.Composer = artists.Name LIMIT 10;

TrackId  Name                                     AlbumId  MediaTypeId  GenreId  Composer                                                      Milliseconds  Bytes     UnitPrice  ArtistId  Name
-------  ---------------------------------------  -------  -----------  -------  ------------------------------------------------------------  ------------  --------  ---------  --------  ----
1        For Those About To Rock (We Salute You)  1        1            1        Angus Young, Malcolm Young, Brian Johnson                     343719        11170334  0.99

2        Balls to the Wall                        2        2            1                                                                      342562        5510424   0.99

3        Fast As a Shark                          3        2            1        F. Baltes, S. Kaufman, U. Dirkscneider & W. Hoffman           230619        3990994   0.99

4        Restless and Wild                        3        2            1        F. Baltes, R.A. Smith-Diesel, S. Kaufman, U. Dirkscneider &   252051        4331779   0.99
                                                                                 W. Hoffman

5        Princess of the Dawn                     3        2            1        Deaffy & R.A. Smith-Diesel                                    375418        6290521   0.99

6        Put The Finger On You                    1        1            1        Angus Young, Malcolm Young, Brian Johnson                     205662        6713451   0.99

7        Let's Get It Up                          1        1            1        Angus Young, Malcolm Young, Brian Johnson                     233926        7636561   0.99

8        Inject The Venom                         1        1            1        Angus Young, Malcolm Young, Brian Johnson                     210834        6852860   0.99

9        Snowballed                               1        1            1        Angus Young, Malcolm Young, Brian Johnson                     203102        6599424   0.99

10       Evil Walks                               1        1            1        Angus Young, Malcolm Young, Brian Johnson                     263497        8611245   0.99

SELECT *
FROM tracks INNER JOIN artists
    ON tracks.Composer = artists.Name LIMIT 10;

TrackId  Name                          AlbumId  MediaTypeId  GenreId  Composer      Milliseconds  Bytes     UnitPrice  ArtistId  Name
-------  ----------------------------  -------  -----------  -------  ------------  ------------  --------  ---------  --------  ------------
15       Go Down                       4        1            1        AC/DC         331180        10847611  0.99       1         AC/DC
16       Dog Eat Dog                   4        1            1        AC/DC         215196        7032162   0.99       1         AC/DC
17       Let There Be Rock             4        1            1        AC/DC         366654        12021261  0.99       1         AC/DC
18       Bad Boy Boogie                4        1            1        AC/DC         267728        8776140   0.99       1         AC/DC
19       Problem Child                 4        1            1        AC/DC         325041        10617116  0.99       1         AC/DC
20       Overdose                      4        1            1        AC/DC         369319        12066294  0.99       1         AC/DC
21       Hell Ain't A Bad Place To Be  4        1            1        AC/DC         254380        8331286   0.99       1         AC/DC
22       Whole Lotta Rosie             4        1            1        AC/DC         323761        10547154  0.99       1         AC/DC
77       Enter Sandman                 9        1            3        Apocalyptica  221701        7286305   0.99       7         Apocalyptica
78       Master Of Puppets             9        1            3        Apocalyptica  436453        14375310  0.99       7         Apocalyptica 


SELECT InvoiceLineId, InvoiceId
FROM invoice_items
ORDER BY InvoiceId LIMIT 5;

SELECT InvoiceId, CustomerId
FROM invoices
ORDER BY InvoiceId LIMIT 5; 

SELECT invoice_items.InvoiceLineId, invoices.InvoiceId
FROM invoice_items INNER JOIN invoices
    ON invoice_items.InvoiceId = invoices.InvoiceId
ORDER BY invoices.InvoiceId DESC LIMIT 5; 

SELECT invoices.InvoiceId, customers.CustomerId
FROM invoices INNER JOIN customers
    ON invoices.CustomerId = customers.CustomerId
ORDER BY invoices.InvoiceId DESC LIMIT 5;


SELECT invoice_items.InvoiceLineId, invoices.InvoiceId, customers.CustomerId 
FROM invoice_items 
    INNER JOIN invoices ON invoice_items.InvoiceId = invoices.InvoiceId
    INNER JOIN customers ON invoices.CustomerId =  customers.CustomerId
ORDER BY invoices.InvoiceId DESC LIMIT 5;

SELECT customers.CustomerId, COUNT(InvoiceLineId) 
FROM invoice_items
    INNER JOIN invoices ON invoice_items.InvoiceId = invoices.InvoiceId
    INNER JOIN customers ON invoices.CustomerId =  customers.CustomerId
GROUP BY customers.CustomerId
ORDER BY customers.CustomerId LIMIT 5;

