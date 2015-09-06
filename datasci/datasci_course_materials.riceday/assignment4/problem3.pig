register s3n://uw-cse-344-oregon.aws.amazon.com/myudfs.jar

-- load the test file into Pig
-- raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/cse344-test-file' USING TextLoader as (line:chararray);
-- later you will load to other files, example:
raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/btc-2010-chunk-000' USING TextLoader as (line:chararray); 

-- parse each line into ntriples
ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);

--group the n-triples by subject column
subgroup = filter ntriples by subject matches '.*rdfabout\\.com.*' PARALLEL 50;

subgroup2 = foreach subgroup generate $0 as subject2, $1 as predicate2, $2 as object2 PARALLEL 50;

joined_subgroups = join subgroup by object, subgroup2 by subject2 PARALLEL 50;
joined_subgroups_distinct = DISTINCT joined_subgroups;

-- store the results in the folder /user/hadoop/example-results
-- store joined_subgroups_distinct into '/tmp/finaloutput' using PigStorage();
store joined_subgroups_distinct into '/user/hadoop/example-results' using PigStorage();
-- Alternatively, you can store the results in S3, see instructions:
-- store count_by_subject_ordered into 's3n://superman/example-results';
