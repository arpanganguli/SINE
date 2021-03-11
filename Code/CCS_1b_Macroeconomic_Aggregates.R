library(ggplot2)
library(plotly)
library(scales)

df <- read.csv("~/Documents/Professional/Projects/SINE/Database/Time_Series/Macroeconomic_Aggregates.csv", stringsAsFactors = TRUE)
View(df)

df <- df[order(df$Year), ]
df$Year <- factor(df$Year, levels = df$Year[order(df$Gross.Domestic.Product)])

p <- ggplot(data = df, aes(x=Year, y=Gross.Domestic.Product)) +
            geom_bar(stat = "identity", fill = "darkblue") +
            theme_minimal() +
            theme(axis.text.x = element_text(face = "bold", color = "#993333", 
                                     size = 12, angle = 45)) +
            labs(title = "Gross Domestic Product \n in Constant Prices (2011)", x = "Year", y = "Gross Domestic Product")
ggplotly(p)