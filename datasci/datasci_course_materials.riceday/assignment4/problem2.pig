register s3n://uw-cse-344-oregon.aws.amazon.com/myudfs.jar

-- load the test file into Pig
-- raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/cse344-test-file' USING TextLoader as (line:chararray);
-- later you will load to other files, example:
raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/btc-2010-chunk-000' USING TextLoader as (line:chararray); 

-- parse each line into ntriples
ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);

--group the n-triples by subject column
subjects = group ntriples by (subject) PARALLEL 50;

count_by_subject = foreach subjects generate flatten($0), COUNT($1) as count PARALLEL 50;

subjects_by_count = group count_by_subject by (count) PARALLEL 50;

subject_count_by_count = foreach subjects_by_count generate flatten($0) as count, COUNT($1) as subject_count PARALLEL 50;

-- store the results in the folder /user/hadoop/example-results
-- store subject_count_by_count into '/tmp/finaloutput' using PigStorage();
store subject_count_by_count into '/user/hadoop/example-results' using PigStorage();
-- Alternatively, you can store the results in S3, see instructions:
-- store count_by_subject_ordered into 's3n://superman/example-results';
