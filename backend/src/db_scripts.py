from typing import List
from sqlalchemy import exc
from sqlalchemy.sql.expression import update

from constants import(
    engine,
    session
)
from data import (
    def_stats,
    kicking_stats,
    player_info,
    commits,
    return_stats,
    off_stats,
    week_year,
    team_info
)
from data_models.DefensiveStats import DefensiveStats
from data_models.PlayerInfo import PlayerInfo
from data_models.TeamInfo import TeamInfo
from helpers import (
    _reformat_column_name,
    _reformat_table_name
    )


def insert_def_stats_into_db(def_stats):
    
    players: List[DefensiveStats] = []

    for i, value in enumerate(def_stats):
        record = def_stats[i]
        
        new_player = DefensiveStats(
            player_id=record.fields['Player ID'],
            long_int_ret=record.fields['Long INT Ret'],
            sacks=record.fields['Sacks'],
            year=record.fields['Year'],
            forced_fumbles=record.fields['Forced Fumbles'],
            solo_tkls=record.fields['Solo Tkls'],
            safeties=record.fields['Safties'],
            pass_def=record.fields['Pass Def.'],
            blocked_kicks=record.fields['Blocked Kicks'],
            tfl=record.fields['TFL'],
            ints_made=record.fields['INTs Made'],
            games_played=record.fields['Games Played'],
            fumbles_rec=record.fields['Fumbles Rec.'],
            half_a_sack=record.fields['Half A Sack'],
            asst_tkls=record.fields['Asst. Tkls'],
            def_tds=record.fields['Def. TDs'],
            fum_rec_yards=record.fields['Fum. Rec. Yards'],
            int_ret_yards=record.fields['INT Ret. Yards']
        )
        players.append(new_player)

    session.add_all(players)
    session.commit()
    session.close()


def insert_player_info_into_db(player_info):
    
    players: List[PlayerInfo] = []
    
    for i, value in enumerate(player_info):
        
        record = player_info[i]
        
        new_player = PlayerInfo(
            player_id=record.fields['Player ID'],
            team_id=record.fields['Team ID'],
            first_name=record.fields['First Name'],
            last_name=record.fields['Last Name'],
            hometown_desc=record.fields['Hometown Desc'],
            play_recognition=record.fields['Play Recognition'],
            press=record.fields['Press'],
            power_moves=record.fields['Power Moves'],
            kick_accuracy=record.fields['Kick Accuracy'],
            redshirt=record.fields['Redshirt'],
            jersey_number=record.fields['Jersey #'],
            throwing_power=record.fields['Throwing Power'],
            throwing_accuracy=record.fields['Throwing Accuracy'],
            overall=record.fields['Overall'],
            agility=record.fields['Agility'],
            stamina=record.fields['Stamina'],
            acceleration=record.fields['Acceleration'],
            pursuit=record.fields['Pursuit'],
            route_running=record.fields['Route Running'],
            speed=record.fields['Speed'],
            trucking=record.fields['Trucking'],
            ball_carrier_vision=record.fields['Ball Carrier Vision'],
            catch_in_traffic=record.fields['Catch In Traffic'],
            block_shedding=record.fields['Block Shedding'],
            strength=record.fields['Strength'],
            catch=record.fields['Catch'],
            injury=record.fields['Injury'],
            tackling=record.fields['Tackling'],
            pass_blocking=record.fields['Pass Blocking'],
            run_blocking=record.fields['Run Blocking'],
            break_tackle=record.fields['Break Tackle'],
            impact_blocking=record.fields['Impact Blocking'],
            jump=record.fields['Jump'],
            carry=record.fields['Carry'],
            stiff_arm=record.fields['Stiff Arm'],
            kick_power=record.fields['Kick Power'],
            awareness=record.fields['Awareness'],
            release=record.fields['Release'],
            position=record.fields['Position'],
            spec_catch=record.fields['Spec Catch'],
            elusiveness=record.fields['Elusiveness'],
            height=record.fields['Height'],
            spin_move=record.fields['Spin Move'],
            weight=record.fields['Weight'],
            hit_power=record.fields['Hit Power'],
            kick_return=record.fields['Kick Return'],
            man_coverage=record.fields['Man Coverage'],
            zone_coverage=record.fields['Zone Coverage'],
            finesse_moves=record.fields['Finesse Moves'],
            juke_move=record.fields['Juke Move'],
            games_played=record.fields['Games Played'],
        )
        players.append(new_player)
    
    try:
        session.add_all(players)
        session.commit()
        session.close()
    except:
        for player in players:
            update(PlayerInfo).where(PlayerInfo.player_id == player.player_id).values(
                player_id=player.player_id,
                team_id=player.team_id,
                first_name=player.first_name,
                last_name=player.last_name,
                hometown_desc=player.hometown_desc,
                play_recognition=player.play_recognition,
                press=player.press,
                power_moves=player.power_moves,
                kick_accuracy=player.kick_accuracy,
                redshirt=player.redshirt,
                jersey_number=player.jersey_number,
                throwing_power=player.throwing_power,
                throwing_accuracy=player.throwing_accuracy,
                overall=player.overall,
                agility=player.agility,
                stamina=player.stamina,
                acceleration=player.acceleration,
                pursuit=player.pursuit,
                route_running=player.route_running,
                speed=player.speed,
                trucking=player.trucking,
                ball_carrier_vision=player.ball_carrier_vision,
                catch_in_traffic=player.catch_in_traffic,
                block_shedding=player.block_shedding,
                strength=player.strength,
                catch=player.catch,
                injury=player.injury,
                tackling=player.tackling,
                pass_blocking=player.pass_blocking,
                run_blocking=player.run_blocking,
                break_tackle=player.break_tackle,
                impact_blocking=player.impact_blocking,
                jump=player.jump,
                carry=player.carry,
                stiff_arm=player.stiff_arm,
                kick_power=player.kick_power,
                awareness=player.awareness,
                release=player.release,
                position=player.position,
                spec_catch=player.spec_catch,
                elusiveness=player.elusiveness,
                height=player.height,
                spin_move=player.spin_move,
                weight=player.weight,
                hit_power=player.hit_power,
                kick_return=player.kick_return,
                man_coverage=player.man_coverage,
                zone_coverage=player.zone_coverage,
                finesse_moves=player.finesse_moves,
                juke_move=player.juke_move,
                games_played=player.games_played,
            )


def insert_team_info_into_db(team_info):
    
    teams: List[TeamInfo] = []
    
    for i, value in enumerate(team_info):
        record = team_info[i]
        
        new_team = TeamInfo(
            team_id=record.fields['Team ID'],
            team_name=record.fields['Team Name'],
            team_short_name=record.fields['Team Short Name'],
            coachs_poll_1st_votes=record.fields["Coach's Poll 1st Votes"],
            nickname=record.fields['Nickname'],
            wins=record.fields['Wins'],
            bcs_rank=record.fields['BCS Rank'],
            coachs_poll_rank=record.fields["Coach's Poll Rank"],
            media_poll_rank=record.fields['Media Poll Rank'],
            losses=record.fields['Losses'],
            media_poll_points=record.fields['Media Poll Points'],
            coachs_poll_points=record.fields["Coach's Poll Points"],
        )
        teams.append(new_team)

    try:
        session.add_all(teams)
        session.commit()
        session.close()
    except:
        for team in teams:
            update(TeamInfo).where(TeamInfo.team_id == team.team_id).values(
                team_id=team.team_id,
                team_name=team.team_name,
                team_short_name=team.team_short_name,
                coachs_poll_1st_votes=team.coachs_poll_1st_votes,
                nickname=team.nickname,
                wins=team.wins,
                bcs_rank=team.bcs_rank,
                coachs_poll_rank=team.coachs_poll_rank,
                media_poll_rank=team.media_poll_rank,
                losses=team.losses,
                media_poll_points=team.media_poll_points,
                coachs_poll_points=team.coachs_poll_points,
            )


def insert_offensive_stats_into_db(off_stats):
    
    pass

