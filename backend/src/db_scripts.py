import ncaa_dynasty
from typing import List
from sqlalchemy import exc
from sqlalchemy.sql.expression import update
from sqlalchemy.sql import exists

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
from data_models.OffensiveStats import OffensiveStats
from data_models.TeamInfo import TeamInfo


def insert_def_stats_into_db(def_stats):

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
        player: DefensiveStats = session.query(DefensiveStats).filter(DefensiveStats.player_id == new_player.player_id).scalar()

        if player is None:
            session.add(new_player)
        else:
            update(DefensiveStats).where(DefensiveStats.player_id == new_player.player_id).values(
                player_id=new_player.player_id,
                long_int_ret=new_player.long_int_ret,
                sacks=new_player.sacks,
                year=new_player.year,
                forced_fumbles=new_player.forced_fumbles,
                solo_tkls=new_player.solo_tkls,
                safeties=new_player.safeties,
                pass_def=new_player.pass_def,
                blocked_kicks=new_player.blocked_kicks,
                tfl=new_player.tfl,
                ints_made=new_player.ints_made,
                games_played=new_player.games_played,
                fumbles_rec=new_player.fumbles_rec,
                half_a_sack=new_player.half_a_sack,
                asst_tkls=new_player.asst_tkls,
                def_tds=new_player.def_tds,
                fum_rec_yards=new_player.fum_rec_yards,
                int_ret_yards=new_player.int_ret_yards
            )
        session.commit()

    session.close()


def insert_off_stats_into_db(off_stats):
    
    for i, value in enumerate(off_stats):
        record = off_stats[i]
        
        new_player = OffensiveStats(
            player_id=record.fields['Player ID'],
            pass_yards=record.fields['Pass. Yards'],
            longest_rec=record.fields['Longest Rec.'],
            longest_pass=record.fields['Longest Pass'],
            longest_run=record.fields['Longest Run'],
            year=record.fields['Year'],
            receptions=record.fields['Receptions'],
            sacked=record.fields['Sacked'],
            rec_yards=record.fields['Rec. Yards'],
            rush_yards=record.fields['Rush Yards'],
            yac=record.fields['Y.A.C.'],
            pass_tds=record.fields['Pass. TDs'],
            games_played=record.fields['Games Played'],
            rec_tds=record.fields['Rec. TDs'],
            rush_tds=record.fields['Rush TDs'],
            ya_contact=record.fields['Y.A. Contact'],
            completions=record.fields['Completions'],
            ints=record.fields['INTs'],
            drops=record.fields['Drops'],
            pass_att=record.fields['Pass Att.'],
            rush_att=record.fields['Rush Att.'],
            broke_tkls=record.fields['Broke Tkls.'],
            fumbles=record.fields['Fumbles'],
            twenty_plus_yd_runs=record.fields['20+ yd. Runs']
        )
        
        player: OffensiveStats = session.query(OffensiveStats).filter(OffensiveStats.player_id == new_player.player_id).scalar()

        if player is None:
            session.add(new_player)
        else:
            update(OffensiveStats).where(OffensiveStats.player_id == new_player.player_id).values(
                player_id=new_player.player_id,
                pass_yards=new_player.pass_yards,
                longest_rec=new_player.longest_rec,
                longest_pass=new_player.longest_pass,
                longest_run=new_player.longest_run,
                year=new_player.year,
                receptions=new_player.receptions,
                sacked=new_player.sacked,
                rec_yards=new_player.rec_yards,
                rush_yards=new_player.rush_yards,
                yac=new_player.yac,
                pass_tds=new_player.pass_tds,
                games_played=new_player.games_played,
                rec_tds=new_player.rec_tds,
                rush_tds=new_player.rush_tds,
                ya_contact=new_player.ya_contact,
                completions=new_player.completions,
                ints=new_player.ints,
                drops=new_player.drops,
                pass_att=new_player.pass_att,
                rush_att=new_player.rush_att,
                broke_tkls=new_player.broke_tkls,
                fumbles=new_player.fumbles,
                twenty_plus_yd_runs=new_player.twenty_plus_yd_runs
            )
        session.commit()

    session.close()


def insert_player_info_into_db(player_info):
    
    players: List[PlayerInfo] = []
    
    for i, value in enumerate(player_info):
        
        record = player_info[i]
        
        # Convert unintelligble values to readable values
        readable_position = ncaa_dynasty.position_number_to_text(record.fields['Position'])
        readable_height = ncaa_dynasty.height_converter(record.fields['Height'])
        readable_weight = ncaa_dynasty.weight_converter(record.fields['Weight'])
        readable_year = ncaa_dynasty.player_year_converter(record.fields['Year'])
        
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
            year=readable_year,
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
            position=readable_position,
            spec_catch=record.fields['Spec Catch'],
            elusiveness=record.fields['Elusiveness'],
            height=readable_height,
            spin_move=record.fields['Spin Move'],
            weight=readable_weight,
            hit_power=record.fields['Hit Power'],
            kick_return=record.fields['Kick Return'],
            man_coverage=record.fields['Man Coverage'],
            zone_coverage=record.fields['Zone Coverage'],
            finesse_moves=record.fields['Finesse Moves'],
            juke_move=record.fields['Juke Move'],
            games_played=record.fields['Games Played'],
        )
        
        player: PlayerInfo = session.query(PlayerInfo).filter(PlayerInfo.player_id == new_player.player_id).scalar()

        if player is None:
            session.add(new_player)
            session.commit()
        else:
            update(PlayerInfo).where(PlayerInfo.player_id == new_player.player_id).values(
                player_id=new_player.player_id,
                team_id=new_player.team_id,
                first_name=new_player.first_name,
                last_name=new_player.last_name,
                hometown_desc=new_player.hometown_desc,
                play_recognition=new_player.play_recognition,
                press=new_player.press,
                power_moves=new_player.power_moves,
                kick_accuracy=new_player.kick_accuracy,
                redshirt=new_player.redshirt,
                year=new_player.year,
                jersey_number=new_player.jersey_number,
                throwing_power=new_player.throwing_power,
                throwing_accuracy=new_player.throwing_accuracy,
                overall=new_player.overall,
                agility=new_player.agility,
                stamina=new_player.stamina,
                acceleration=new_player.acceleration,
                pursuit=new_player.pursuit,
                route_running=new_player.route_running,
                speed=new_player.speed,
                trucking=new_player.trucking,
                ball_carrier_vision=new_player.ball_carrier_vision,
                catch_in_traffic=new_player.catch_in_traffic,
                block_shedding=new_player.block_shedding,
                strength=new_player.strength,
                catch=new_player.catch,
                injury=new_player.injury,
                tackling=new_player.tackling,
                pass_blocking=new_player.pass_blocking,
                run_blocking=new_player.run_blocking,
                break_tackle=new_player.break_tackle,
                impact_blocking=new_player.impact_blocking,
                jump=new_player.jump,
                carry=new_player.carry,
                stiff_arm=new_player.stiff_arm,
                kick_power=new_player.kick_power,
                awareness=new_player.awareness,
                release=new_player.release,
                position=new_player.position,
                spec_catch=new_player.spec_catch,
                elusiveness=new_player.elusiveness,
                height=new_player.height,
                spin_move=new_player.spin_move,
                weight=new_player.weight,
                hit_power=new_player.hit_power,
                kick_return=new_player.kick_return,
                man_coverage=new_player.man_coverage,
                zone_coverage=new_player.zone_coverage,
                finesse_moves=new_player.finesse_moves,
                juke_move=new_player.juke_move,
                games_played=new_player.games_played,
            )
        session.commit()

    session.close()



def insert_team_info_into_db(team_info):
    
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
        
        team: TeamInfo = session.query(TeamInfo).filter(TeamInfo.team_id == new_team.team_id).scalar()
        
        if team is None:
            session.add(new_team)
            session.commit()
        else:
            update(TeamInfo).where(TeamInfo.team_id == new_team.team_id).values(
                team_id=new_team.team_id,
                team_name=new_team.team_name,
                team_short_name=new_team.team_short_name,
                coachs_poll_1st_votes=new_team.coachs_poll_1st_votes,
                nickname=new_team.nickname,
                wins=new_team.wins,
                bcs_rank=new_team.bcs_rank,
                coachs_poll_rank=new_team.coachs_poll_rank,
                media_poll_rank=new_team.media_poll_rank,
                losses=new_team.losses,
                media_poll_points=new_team.media_poll_points,
                coachs_poll_points=new_team.coachs_poll_points,
            )
            session.commit()
    session.close()



