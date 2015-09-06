select count(docid) from (select docid, sum(count) as term_count from frequency group by docid) where term_count > 300;
