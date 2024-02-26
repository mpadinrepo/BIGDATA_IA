userID = LOAD '/media/exame/PIG/ml-100k/users-vip.data2.txt' USING PigStorage (',')
as
(userID:int,gender:chararray,age:int,occupation:chararray,zip-code:int);

dump userID;
