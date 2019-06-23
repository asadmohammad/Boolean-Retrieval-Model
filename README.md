# Boolean Retrieval Model

INTRODUCTION
 ------------

The (standard) Boolean model of information retrieval (BIR) is a classical information retrieval (IR) model and, at the same time, the first and most-adopted one. It is used by many IR systems to this day.The BIR is based on Boolean logic and classical set theory in that both the documents to be searched and the user's query are conceived as sets of terms. Retrieval is based on whether or not the documents contain the query terms.



REQUIREMENTS
 ------------

Following are the reuirements to run this project:
i. Python version 3.x (Anaconda)


DATASETS
--------
A single file contains 50 pen
crafts of stories for children.
It is recommended to first review the given text files for indexing. Each file contains
a single story; the first line contains the name of the story. The second line contains
the author-name You need to treat each as a unique document. If there is any extra
header and footers for each pen craft, it need to be filter and only get the content of
it will be challenging.

Query Processing
----------------
All you need to implement an information retrieval model called
Boolean Information Retrieval Model with some simplified assumptions. You need
to treat each story as a document and need to index it content separately. There are
50 documents. you need to implement a simplified Boolean user queries that can
only be formed by joining three terms (t1, t2 and t3) with (AND, OR and NOT)
Boolean operators. For example a user query may be of the form (t1 AND t2 AND
t3). For positional queries, the query text contains “/” along with a k intended to
return all documents that contains t1 and t2, k words apart on either side of the text.


ASSUMPTIONS
-----------
1. An index term (word) is either present (1) or absent (0) in the document. A
dictionary contains all index terms.
2. All index terms provide equal evidence with respect to information needs. (
No frequency count necessary, but in next assignment it can be)
3. Queries are Boolean combinations of index terms (at max 3).
4. Boolean Operators (AND, OR and NOT) are allowed. For examples:
X AND Y: represents doc that contains both X and Y
X OR Y: represents doc that contains either X or Y
NOT X: represents the doc that do not contain X
5. Queries of the type X AND Y / 3 represents doc that contains both X and Y
and 3 words apart.
