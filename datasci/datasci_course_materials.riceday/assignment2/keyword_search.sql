drop view frequency_with_q;
create view frequency_with_q as SELECT * FROM frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION
SELECT 'q' as docid, 'treasury' as term, 1 as count;

select docid2, similarity from (select t1.docid as docid1, t2.docid as docid2, sum(t1.count * t2.count) as similarity from frequency_with_q t1, frequency_with_q t2 where t1.term = t2.term group by docid1, docid2) where docid1 = 'q' order by similarity;
