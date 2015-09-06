select count(*) from (select docid from frequency where term = 'transactions') as t1 join (select docid from frequency where term = 'world') as t2 where t1.docid = t2.docid;
