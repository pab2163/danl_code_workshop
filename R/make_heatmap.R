library(tidyverse)
library(heatmap3)
library(viridis)


# remove any existing plots, read in data
dev.off()
df = read_csv('../data/familiar_music_database.csv')


# scale all variables, select first 20 observations
df_heatmap = dplyr::select(df, danceability, mode, energy, valence, loudness, tempo, speechiness, liveness) %>%
  dplyr::mutate_all(scale) 


# convert dataframe to matrix (needed to make a heatmap)
heatmap_matrix = as.matrix(df_heatmap)

# assign the titles of the songs as the matrix row names
row.names(heatmap_matrix) = df$title[1:nrow(df_heatmap)]


# make heatmap using heatmap3()
heatmap3(heatmap_matrix, scale = 'column', col = viridis(256), margins= c(8, 20))
