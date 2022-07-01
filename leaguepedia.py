import mwclient
site = mwclient.Site('lol.fandom.com', path='/')

response = site.api('cargoquery',
	limit = 30,
	tables = "MatchSchedule=MS",
	fields = "MS.DateTime_UTC, MS.Team1, MS.Team2",
    where = "MS.ShownName='LFL 2022 Summer' AND (MS.Team1='Karmine Corp' OR MS.Team2='Karmine Corp') ",
)['cargoquery']       

