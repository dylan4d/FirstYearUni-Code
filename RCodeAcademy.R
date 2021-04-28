---
title: "ACLU Child Separations"
output: html_notebook
---

```{r message=FALSE, warning=FALSE, error=TRUE}
# load libraries
library(readr)
library(dplyr)

```

```{r error=TRUE}
# load data
aclu <- read_csv('aclu_separations.csv')
```

```{r error=TRUE}
# inspect data
head(aclu)
summary(aclu)

```

```{r error=TRUE}
# select columns
aclu <- select(aclu, -addr)

```

```{r error=TRUE}
# view columns
colnames(aclu)
```

```{r error=TRUE}
# rename columns
aclu <- aclu %>%
rename(city = program_city, state = program_state, number_children = n, longitude = lon, latitude = lat)

colnames(aclu)

```

```{r error=TRUE}
# add column
border_latitude <- 25.83



```

```{r error=TRUE}
# latitude change
aclu <- aclu %>%
mutate(lat_change_border = latitude - border_latitude)

further_away <- aclu %>%
filter(lat_change_border > 15) %>%
arrange(desc(lat_change_border))

head(further_away)
```

```{r error=TRUE}
# number of children
ordered_by_children <- aclu %>%
arrange(desc(number_children))

head(ordered_by_children)
```

```{r error=TRUE}
# state analysis
chosen_state <-  'TX'

chosen_state_separations <- aclu %>%
filter(state == chosen_state) %>%
arrange(desc(number_children))
head(chosen_state_separations)

```
