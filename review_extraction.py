__author__ = 'Carmen Dolling, cdolling@live.unc.edu, Onyen = cdolling'
import pandas as pd
import numpy as np

# variables for the file names, so the code can easily be run again with new files
import_file = "Italian.csv"
export_json = "Italian_reviews.JSON"
export_csv = "Italian_reviews.csv"

# import the cuisine csv
business_df = pd.read_csv(import_file)

# extract only the business IDs for the cuisine, and convert to a list
business_ids = business_df['business_id'].tolist()
print(business_ids)

# create an empty dataframe, to which we will later append the relevant reviews
reviews_list = pd.DataFrame()

# initialize a counter for the chunks
ctr=0

# read in the review json file, chunking by 100,000 lines at a time
for reviews_chunk in pd.read_json("yelp_academic_dataset_review.json", lines=True, chunksize=100000):
    # update the counter for each chunk loop, print the number, and view the chunk size
    ctr+=1
    print("This is chunk number: " + str(ctr))
    print(reviews_chunk.shape)
    print("************")
    # save a copy of the chunk into its own new dataframe and reset the index to 0
    chunk_df = reviews_chunk
    chunk_df = chunk_df.reset_index(drop=True)

    # loop over each business ID in the list
    for i in business_ids:
        print("Printing for business: " + str(i))

        # create a boolean true-false 'list'(?) for rows in the chunk whose business ID matches the active i
        is_in_set = [chunk_df['business_id'].isin([i])]

        # store the rows (in the current chunk) for which the business_id-match is true
        true_list = np.where(is_in_set[:1])

        # create an actual list of the indexes (in the current chunk) for those rows
        indices = true_list[1].tolist()

        # print the list of indexes (in the current chunk) for which a match was found
        # (in other words, the indexes to the rows/reviews for a business matching the given set)
        print("List of matching indices: " + str(indices))
        print("Number of matching indices found: " + str(len(indices)))
        print("-----------------")

        # loop over each identified match in the set of indexes (which belong to the chunk)
        for j in indices:

            # handle errors if an index is not found
            try:
                # use a new variable to store the review (in the chunk) at index j
                set_chunk_df = chunk_df.loc[j]

                # append that review to the master list of reviews
                reviews_list = reviews_list.append(set_chunk_df,ignore_index=True)

                # print the individual review to the screen
                # print(set_chunk_df)

            except:
                print("index " + str(j) + " could not be found in this chunk.")
            print("::::::::::::::::::")

# export the master dataframe (of matching reviews) to json and csv formats
reviews_list.to_json(export_json)
reviews_list.to_csv(export_csv)