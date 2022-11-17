import requests
import json
from flask_app import app, bcrypt, TEAMVALS
from flask import render_template, redirect, request, session, flash, jsonify
from flask_app.models.player import Player
from flask_app.models.team import Team
from flask_app.models.roster import Roster

@app.route('/')
def home():
    return render_template('landing_page.html')


@app.route('/import')
def import_league():
    league = []
    teams = []
    teams_in_league = []
    if "league_id" in session:

        league_id = session["league_id"]
        leauge_req = requests.get(
            f"https://api.sleeper.app/v1/league/{league_id}")
        if leauge_req:
            league = json.loads(leauge_req.content)


        teams_req = requests.get(
            f"https://api.sleeper.app/v1/league/{league_id}/users")
        if teams_req:
            teams = json.loads(teams_req.content)
            teams_in_league = []
            for team in teams:
                team = Team(team)
                teams_in_league.append(team)

        rosters_req = requests.get(
            f"https://api.sleeper.app/v1/league/{league_id}/rosters")
        if rosters_req:
            rosters = json.loads(rosters_req.content)
            for roster in rosters:
                roster = Roster(roster)
                players_on_roster = []
                for player in roster.players:
                    player = Player.get_one({"player_id": int(player)})
                    print(player.depth_chart_order, "********************")
                    print(type(player.depth_chart_order), "********************")
                    players_on_roster.append(player)
                for team in teams_in_league:
                    if roster.owner_id == team.user_id:
                        team.roster = players_on_roster
                        continue

    return render_template("league_display.html", league=league, teams=teams_in_league)


@app.route('/get_league', methods=["POST"])
def get_league():

    session["league_id"] = request.form['league_id']
    return redirect("/import")


@app.route('/calculator')
def trade_calc():
    players = Player.get_all()
    RBs = []
    QBs = []
    TEs = [] 
    WRs = []

    for player in players:
        if player.position == 'TE':
            TEs.append(player)
        elif player.position == 'WR':
            WRs.append(player)
        elif player.position == 'QB':
            QBs.append(player)
        elif player.position == 'RB':
            RBs.append(player)
        


    return render_template("trade_calc.html", RBs = RBs, QBs = QBs, TEs = TEs, WRs = WRs, all_players = players)

@app.route('/clear')
def clear_session():
    session.clear()
    return render_template("league_display.html")



