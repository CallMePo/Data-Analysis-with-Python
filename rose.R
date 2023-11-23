library(magrittr)
library(ggfx)
library(ggplot2)
library(tidyverse)
seq(-3, 3, by = .02) %>%
  expand.grid(x = ., y = .) %>%
  ggplot(aes(x = (1 - x - sin(y ^ 2)), y = (1 + y - cos(x ^ 2)))) +
  ggfx::with_outer_glow(
    geom_point(
      alpha = .05,
      shape = 20,
      size = 0,
      color = "deeppink"
    ),
    colour = "purple",
    expand = 10,
    sigma = 3
  ) +
  theme_void() +
  coord_polar()