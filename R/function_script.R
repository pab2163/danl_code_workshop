library(tidyverse)

search_artist = function(artist_name, data_frame){
  artist_name = tolower(artist_name)
  output_df = dplyr::filter(data_frame, tolower(artist) == artist_name)
  if (nrow(output_df) > 0){
    return(output_df)
  }
  else{
    return("No match found")
  }
}


custom_addition = function(number_a, number_b){
  total = number_a + number_b
  hi = 'my_string'
  return(total)
}

greet = function(person_name){
  # inside
  print(paste0('Hi: ', person_name))
}

sum_plus_one = Vectorize(function (numbers) {
  sum =  sum(numbers)
  return(sum + 1)
})