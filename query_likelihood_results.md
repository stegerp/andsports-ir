# Retrieval results for the Query Likelihood draft implementation

The data prepared for the queries below is based on the following SQL statement:

`select DISTINCT profile.url_andsports as 'andpsorts url', profile.description as 'profile description'
 from profile
 where profile.language_id = 'es'
 order by profile.url_andsports`
 
For this test, information about profile name, sports and locations has not been exported from DB explicitly. I.e., ideally, the query results
below only reflect content that is part of each profile description itself.

Check the profiles to verify your results. It´s fun.

Sometimes, I don´t find the profiles in andsports.com easily, so I google them like "andsports.com" plus the andsports url or I use our filter,
https://www.andsports.com/en/filter-cities-and-sports, which still does a good job :)

## Queries

### quiero jugar al fútbol en Barcelona
| andsports url 	| score 	|
|----------------------------------------	|--------------------	|
| club-osos-rugby-subacuatico-madrid 	| 0.9668325078500167 	|
| futbol-club-barcelona 	| 0.9663514916265883 	|
| barcelona-eagles-cricket-club 	| 0.9646203903700339 	|
| club-bcn-rugby-subaquatic 	| 0.9637194271960008 	|
| campo-de-futbol-de-la-ciudad-deportiva 	| 0.9635697663936815 	|
| campo-de-futbol-del-garbinet 	| 0.9635697663936815 	|
| campo-de-futbol-florida-babel 	| 0.9635697663936815 	|
| campo-de-futbol-la-albufereta 	| 0.9635697663936815 	|
| campo-de-futbol-virgen-del-remedio 	| 0.9635697663936815 	|
| club-polideportivo-ejido 	| 0.9635697663936815 	|
https://alcorcon.andsports.com/es/club-osos-rugby-subacuatico-madrid (prevails *querer* and *jugar*)

### karate en un gimnasio
| andsports url 	| score 	|
|--------------------------------------------	|--------------------	|
| gimnasio-karate-kan 	| 0.9882898282581238 	|
| gimnasio-del-estadio-de-atletismo 	| 0.9862824666971532 	|
| zeus-gym-club 	| 0.9856560137919209 	|
| nick-esports 	| 0.985212109514075 	|
| club-de-judo-sant-jordi 	| 0.9849186970966648 	|
| pabellon-municipal-floriba-babel 	| 0.9848681825238076 	|
| club-karate-sant-cugat 	| 0.9846379334975595 	|
| karate-terrassa 	| 0.9846379334975595 	|
| gimnasio-do-chan 	| 0.9843503674828764 	|
| gimnasio-extreme 	| 0.9843503674828764 	|
https://zaragoza.andsports.com/es/gimnasio-karate-kan (no comment)

### bailar como un indio
| andsports url 	| score 	|
|--------------------------------	|--------------------	|
| river-guru 	| 0.980167486231164 	|
| ines-e-inigo-dantza-eskola 	| 0.9799702045176526 	|
| cbd-cinco-puntos 	| 0.9798596280010382 	|
| lindyhopcat---escuela-de-baile 	| 0.979629230088198 	|
| sei-shin-ryu-karate-do 	| 0.9795063224706119 	|
| aradance-cbd 	| 0.9794160037003409 	|
| flaixdansa 	| 0.9787346720124948 	|
| gimnasio-bravo-murillo-fitness 	| 0.9786527200898911 	|
| club-impulso-urbano 	| 0.9783636976000933 	|
| escuela-de-danza-madrid-47 	| 0.9779634628416876 	|
https://jaca.andsports.com/es/river-guru (my favourite, do you see it :-))


Try out yourselve!
 
 <!-- 
 https://www.tablesgenerator.com/markdown_tabless
 -->
