from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile, Form
from sqlalchemy.orm import Session
from typing import List
import service, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/communities/')
async def post_communities(raw_data: schemas.PostCommunities, headers: Request, db: Session = Depends(get_db)):
    try:
        return await service.post_communities(db, raw_data, headers)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/community_users/')
async def post_community_users(raw_data: schemas.PostCommunityUsers, db: Session = Depends(get_db)):
    try:
        return await service.post_community_users(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/user/')
async def post_user(raw_data: schemas.PostUser, db: Session = Depends(get_db)):
    try:
        return await service.post_user(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/login')
async def post_login(raw_data: schemas.PostLogin, db: Session = Depends(get_db)):
    try:
        return await service.post_login(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/communities/')
async def get_communities(db: Session = Depends(get_db)):
    try:
        return await service.get_communities(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/date/')
async def get_date(db: Session = Depends(get_db)):
    try:
        return await service.get_date(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/image/')
async def get_image(db: Session = Depends(get_db)):
    try:
        return await service.get_image(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/image/id')
async def get_image_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_image_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/image/')
async def post_image(raw_data: schemas.PostImage, db: Session = Depends(get_db)):
    try:
        return await service.post_image(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/image/id/')
async def put_image_id(id: int, ratio: str, url: str, width: int, height: int, fallback: str, event_id: str, db: Session = Depends(get_db)):
    try:
        return await service.put_image_id(db, id, ratio, url, width, height, fallback, event_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/image/id')
async def delete_image_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_image_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/event/')
async def get_event(db: Session = Depends(get_db)):
    try:
        return await service.get_event(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/event/id')
async def get_event_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_event_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/event/')
async def post_event(raw_data: schemas.PostEvent, db: Session = Depends(get_db)):
    try:
        return await service.post_event(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/event/id/')
async def put_event_id(id: int, name: str, type: str, url: str, locale: str, segment: str, genre: str, sub_genre: str, event_type: str, sub_type: str, min_price: str, max_price: str, currency_type: str, seatmap_url: str, safe_tix: str, min_age: int, ticket_limit: str, accessibility_limit: str, all_inclusive_pricing: str, created_at: str, updated_at: str, date_id: int, venue_id: int, event_id: str, is_trending: str, is_active: str, db: Session = Depends(get_db)):
    try:
        return await service.put_event_id(db, id, name, type, url, locale, segment, genre, sub_genre, event_type, sub_type, min_price, max_price, currency_type, seatmap_url, safe_tix, min_age, ticket_limit, accessibility_limit, all_inclusive_pricing, created_at, updated_at, date_id, venue_id, event_id, is_trending, is_active)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/event/id')
async def delete_event_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_event_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/date/id')
async def get_date_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_date_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/date/')
async def post_date(raw_data: schemas.PostDate, db: Session = Depends(get_db)):
    try:
        return await service.post_date(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/date/id/')
async def put_date_id(id: int, timezone: str, status: str, span_multiple_days: str, local_date: str, local_time: str, datetime: str, date_tbd: str, date_tba: str, time_tba: str, no_specific_time: str, db: Session = Depends(get_db)):
    try:
        return await service.put_date_id(db, id, timezone, status, span_multiple_days, local_date, local_time, datetime, date_tbd, date_tba, time_tba, no_specific_time)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/date/id')
async def delete_date_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_date_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/venue/')
async def get_venue(db: Session = Depends(get_db)):
    try:
        return await service.get_venue(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/venue/id')
async def get_venue_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_venue_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/posts/id')
async def delete_posts_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_posts_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/venue/')
async def post_venue(raw_data: schemas.PostVenue, db: Session = Depends(get_db)):
    try:
        return await service.post_venue(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/venue/id/')
async def put_venue_id(id: int, name: str, type: str, url: str, locale: str, postal_code: str, timezone: str, city: str, state: str, country: str, country_code: str, address_line1: str, longitude: float, latitude: float, phone_number_detail: str, open_hours_detail: str, accepted_payment_detail: str, will_call_detail: str, created_at: str, updated_at: str, db: Session = Depends(get_db)):
    try:
        return await service.put_venue_id(db, id, name, type, url, locale, postal_code, timezone, city, state, country, country_code, address_line1, longitude, latitude, phone_number_detail, open_hours_detail, accepted_payment_detail, will_call_detail, created_at, updated_at)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/venue/id')
async def delete_venue_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_venue_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/posts_like/')
async def get_posts_like(db: Session = Depends(get_db)):
    try:
        return await service.get_posts_like(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/posts_like/id')
async def get_posts_like_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_posts_like_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/posts_like/')
async def post_posts_like(raw_data: schemas.PostPostsLike, db: Session = Depends(get_db)):
    try:
        return await service.post_posts_like(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/posts_like/id/')
async def put_posts_like_id(id: int, user_id: str, post_id: str, reaction_alias: str, db: Session = Depends(get_db)):
    try:
        return await service.put_posts_like_id(db, id, user_id, post_id, reaction_alias)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/posts_like/id')
async def delete_posts_like_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_posts_like_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/posts/')
async def get_posts(db: Session = Depends(get_db)):
    try:
        return await service.get_posts(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/posts/id')
async def get_posts_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_posts_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/posts/')
async def post_posts(raw_data: schemas.PostPosts, db: Session = Depends(get_db)):
    try:
        return await service.post_posts(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/posts/id/')
async def put_posts_id(id: int, post_id: str, community_id: str, user_id: str, caption: str, image: str, status_alias: str, created_at: str, updated_at: str, post_type: str, ref_event_id: str, db: Session = Depends(get_db)):
    try:
        return await service.put_posts_id(db, id, post_id, community_id, user_id, caption, image, status_alias, created_at, updated_at, post_type, ref_event_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/communities/id')
async def get_communities_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_communities_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/communities/id/')
async def put_communities_id(id: int, community_id: str, name: str, description: str, image: str, category: str, type: str, admin_id: str, status_alias: str, created_at: str, updated_at: str, is_active: str, db: Session = Depends(get_db)):
    try:
        return await service.put_communities_id(db, id, community_id, name, description, image, category, type, admin_id, status_alias, created_at, updated_at, is_active)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/communities/id')
async def delete_communities_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_communities_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/user/')
async def get_user(db: Session = Depends(get_db)):
    try:
        return await service.get_user(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/user/user_id')
async def get_user_user_id(user_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_user_user_id(db, user_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/user/user_id/')
async def put_user_user_id(user_id: str, name: str, email: str, phone: str, country_code: str, login_type: str, google_id: str, apple_id: str, created_at: str, updated_at: str, gender: str, id: int, streak: int, last_login: str, user_avatar: str, is_blocked: str, db: Session = Depends(get_db)):
    try:
        return await service.put_user_user_id(db, user_id, name, email, phone, country_code, login_type, google_id, apple_id, created_at, updated_at, gender, id, streak, last_login, user_avatar, is_blocked)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/user/user_id')
async def delete_user_user_id(user_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_user_user_id(db, user_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/attraction/')
async def get_attraction(db: Session = Depends(get_db)):
    try:
        return await service.get_attraction(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/attraction/id')
async def get_attraction_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_attraction_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/crm_users/')
async def post_crm_users(raw_data: schemas.PostCrmUsers, headers: Request, db: Session = Depends(get_db)):
    try:
        return await service.post_crm_users(db, raw_data, headers)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/attraction/id/')
async def put_attraction_id(id: int, name: str, url: str, event_id: str, db: Session = Depends(get_db)):
    try:
        return await service.put_attraction_id(db, id, name, url, event_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/attraction/id')
async def delete_attraction_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_attraction_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/crm_users/')
async def get_crm_users(db: Session = Depends(get_db)):
    try:
        return await service.get_crm_users(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/crm_users/id')
async def get_crm_users_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_crm_users_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/reward/id')
async def delete_reward_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_reward_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/crm_users/id/')
async def put_crm_users_id(id: int, crm_id: str, name: str, email: str, password: str, recovery_number: str, designation: str, department: str, role: str, created_at: str, updated_at: str, is_blocked: str, db: Session = Depends(get_db)):
    try:
        return await service.put_crm_users_id(db, id, crm_id, name, email, password, recovery_number, designation, department, role, created_at, updated_at, is_blocked)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/crm_users/id')
async def delete_crm_users_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_crm_users_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/reward/')
async def get_reward(db: Session = Depends(get_db)):
    try:
        return await service.get_reward(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/reward/id')
async def get_reward_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_reward_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/reward/')
async def post_reward(raw_data: schemas.PostReward, db: Session = Depends(get_db)):
    try:
        return await service.post_reward(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/reward/id/')
async def put_reward_id(id: int, reward_id: str, name: str, alias: str, reward_on: str, value: str, frequency: int, img_url: str, creted_at: str, updated_at: str, reward_type: str, earn_bonus: str, sub_description: str, is_active: str, db: Session = Depends(get_db)):
    try:
        return await service.put_reward_id(db, id, reward_id, name, alias, reward_on, value, frequency, img_url, creted_at, updated_at, reward_type, earn_bonus, sub_description, is_active)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/question_master/')
async def get_question_master(db: Session = Depends(get_db)):
    try:
        return await service.get_question_master(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/question_master/id')
async def get_question_master_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_question_master_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/question_master/')
async def post_question_master(raw_data: schemas.PostQuestionMaster, db: Session = Depends(get_db)):
    try:
        return await service.post_question_master(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/question_master/id/')
async def put_question_master_id(type: str, question: str, status: str, created_at: str, updated_at: str, created_by: str, updated_by: str, is_active: str, min_range: int, max_range: int, id: int, db: Session = Depends(get_db)):
    try:
        return await service.put_question_master_id(db, type, question, status, created_at, updated_at, created_by, updated_by, is_active, min_range, max_range, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/question_master/id')
async def delete_question_master_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_question_master_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/user_sessions/')
async def get_user_sessions(db: Session = Depends(get_db)):
    try:
        return await service.get_user_sessions(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/community_users/')
async def get_community_users(db: Session = Depends(get_db)):
    try:
        return await service.get_community_users(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/user_sessions/session_id')
async def get_user_sessions_session_id(session_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_user_sessions_session_id(db, session_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/user_sessions/')
async def post_user_sessions(raw_data: schemas.PostUserSessions, db: Session = Depends(get_db)):
    try:
        return await service.post_user_sessions(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/user_sessions/session_id/')
async def put_user_sessions_session_id(session_id: str, user_id: str, device_type: str, device_id: str, app_version: str, os_version: str, access_token: str, refresh_token: str, ip_address: str, user_agent: str, location: str, login_time: str, last_activity: str, expiration_time: str, status: str, created_at: str, updated_at: str, db: Session = Depends(get_db)):
    try:
        return await service.put_user_sessions_session_id(db, session_id, user_id, device_type, device_id, app_version, os_version, access_token, refresh_token, ip_address, user_agent, location, login_time, last_activity, expiration_time, status, created_at, updated_at)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/user_sessions/session_id')
async def delete_user_sessions_session_id(session_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_user_sessions_session_id(db, session_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/user_bucketlist/')
async def get_user_bucketlist(db: Session = Depends(get_db)):
    try:
        return await service.get_user_bucketlist(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/user_bucketlist/id')
async def get_user_bucketlist_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_user_bucketlist_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/user_bucketlist/')
async def post_user_bucketlist(raw_data: schemas.PostUserBucketlist, db: Session = Depends(get_db)):
    try:
        return await service.post_user_bucketlist(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/user_bucketlist/id/')
async def put_user_bucketlist_id(user_id: str, event_id: str, has_booked: str, booked_time: str, created_at: str, id: int, db: Session = Depends(get_db)):
    try:
        return await service.put_user_bucketlist_id(db, user_id, event_id, has_booked, booked_time, created_at, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/user_bucketlist/id')
async def delete_user_bucketlist_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_user_bucketlist_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/user_survey/')
async def get_user_survey(db: Session = Depends(get_db)):
    try:
        return await service.get_user_survey(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/user_survey/id')
async def get_user_survey_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_user_survey_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/user_survey/')
async def post_user_survey(raw_data: schemas.PostUserSurvey, db: Session = Depends(get_db)):
    try:
        return await service.post_user_survey(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/user_survey/id/')
async def put_user_survey_id(created_at: str, updated_at: str, user_id: str, id: int, question_id: int, answer_id: int, db: Session = Depends(get_db)):
    try:
        return await service.put_user_survey_id(db, created_at, updated_at, user_id, id, question_id, answer_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/user_survey/id')
async def delete_user_survey_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_user_survey_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/user_reward/')
async def get_user_reward(db: Session = Depends(get_db)):
    try:
        return await service.get_user_reward(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/user_reward/id')
async def get_user_reward_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_user_reward_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/user_reward/')
async def post_user_reward(raw_data: schemas.PostUserReward, db: Session = Depends(get_db)):
    try:
        return await service.post_user_reward(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/user_reward/id/')
async def put_user_reward_id(id: int, user_id: str, reward_id: str, reward_value: int, creted_at: str, updated_at: str, is_visible: str, db: Session = Depends(get_db)):
    try:
        return await service.put_user_reward_id(db, id, user_id, reward_id, reward_value, creted_at, updated_at, is_visible)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/user_reward/id')
async def delete_user_reward_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_user_reward_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/user_events/')
async def get_user_events(db: Session = Depends(get_db)):
    try:
        return await service.get_user_events(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/user_events/id')
async def get_user_events_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_user_events_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/user_events/')
async def post_user_events(raw_data: schemas.PostUserEvents, db: Session = Depends(get_db)):
    try:
        return await service.post_user_events(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/user_events/id/')
async def put_user_events_id(id: int, user_id: str, event_id: str, created_at: str, updated_at: str, db: Session = Depends(get_db)):
    try:
        return await service.put_user_events_id(db, id, user_id, event_id, created_at, updated_at)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/user_events/id')
async def delete_user_events_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_user_events_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/community_users/id')
async def get_community_users_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_community_users_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/community_users/id/')
async def put_community_users_id(id: int, community_id: str, user_id: str, created_at: str, updated_at: str, blocked: str, db: Session = Depends(get_db)):
    try:
        return await service.put_community_users_id(db, id, community_id, user_id, created_at, updated_at, blocked)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/community_users/id')
async def delete_community_users_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_community_users_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/post_comments/')
async def get_post_comments(db: Session = Depends(get_db)):
    try:
        return await service.get_post_comments(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/post_comments/id')
async def get_post_comments_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_post_comments_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/post_comments/id/')
async def put_post_comments_id(id: int, comment_id: str, post_id: str, user_id: str, comment: str, status_alias: str, created_at: str, updated_at: str, db: Session = Depends(get_db)):
    try:
        return await service.put_post_comments_id(db, id, comment_id, post_id, user_id, comment, status_alias, created_at, updated_at)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/post_comments/id')
async def delete_post_comments_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_post_comments_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/post_comments/')
async def post_post_comments(raw_data: schemas.PostPostComments, headers: Request, db: Session = Depends(get_db)):
    try:
        return await service.post_post_comments(db, raw_data, headers)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/attraction/')
async def post_attraction(raw_data: schemas.PostAttraction, headers: Request, db: Session = Depends(get_db)):
    try:
        return await service.post_attraction(db, raw_data, headers)
    except Exception as e:
        raise HTTPException(500, str(e))

