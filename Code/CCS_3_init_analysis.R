library(RSQLite)

filename <- "/Users/arpanganguli/Documents/Professional/Projects/SINE/Database/CCS.db"
sqlite.driver <- dbDriver("SQLite")
db <- dbConnect(sqlite.driver, dbname=filename)
dbListTables(db)
myTable <- dbReadTable(db, "CCS")

View(myTable)

Delhi <- dbGetQuery(db, 'SELECT * FROM CCS WHERE City="Delhi"')
View(Delhi)