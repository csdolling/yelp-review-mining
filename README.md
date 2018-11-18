# yelp-review-mining

Work completed so far:

I. Yelp business extraction:
  1. filtered down by location (AZ had the most businesses by far)
  2. filtered down to only businesses with > 100 reviews
  3. broken out into separate sets by cuisine (tried various; only chose those with > 100 businesses)
      1. American (995)
      2. Mexican (440)
      3. Italian (342)
      4. Chinese (191)
      5. Japanese (172)
      6. Mediterranean (139)
      7. Thai (112)
  4. saved each cuisine set to its own csv & json file
 
 
Work to do: 
  
II. Yelp review extraction
  1. need to chunk up the file because it's too large to read in
  2. then filter out only reviews with AZ for state
    1. hopefully this set will be small enough that we can put these AZ reviews back together into one file, which will be way easier to work with
  3. then write a program which reads in the AZ reviews file and a cuisine file
    1. for each business id in the cuisine file, search the review file for all reviews for that business, and write these to new file
    2. do this for each cuisine
    3. we should end with separate files of all reviews per cuisine (for the chosen list of businesses)
    
III. develop a classifier
  1. maybe someone can start working on this? we can do the conceptual work even without the data in hand yet
