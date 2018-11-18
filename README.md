# yelp-review-mining

Work completed so far:

1. Yelp business extraction
  -filtered down by location (AZ had the most businesses by far)
  -filtered down to only businesses with > 100 reviews
  -broken out into separate sets by cuisine
    -tried various popular cuisines; only chose those with over 100 businesses in the set
      -American (995)
      -Mexican (440)
      -Italian (342)
      -Chinese (191)
      -Japanese (172)
      -Mediterranean (139)
      -Thai (112)
  -saved each cuisine set to its own csv & json file
 
 
Work to do: 
  
2. Yelp review extraction
  -need to chunk up the file because it's too large to read in
  -then filter out only reviews with AZ for state
    -hopefully this set will be small enough that we can put these AZ reviews back together into one file, which will be way easier to work with
  -then write a program which reads in the AZ reviews file and a cuisine file
    -for each business id in the cuisine file, search the review file for all reviews for that business, and write these to new file
    -do this for each cuisine
    -we should end with separate files of all reviews per cuisine (for the chosen list of businesses)
    
3. develop a classifier
  -maybe someone can start working on this? we can do the conceptual work even without the data in hand yet
