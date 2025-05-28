from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3

import jwt

import datetime

from pathlib import Path

async def post_communities(db: Session, raw_data: schemas.PostCommunities , request: Request):
    id:int = raw_data.id
    community_id:str = raw_data.community_id
    name:str = raw_data.name
    description:str = raw_data.description
    image:str = raw_data.image
    category:str = raw_data.category
    type:str = raw_data.type
    admin_id:str = raw_data.admin_id
    status_alias:str = raw_data.status_alias
    created_at:str = raw_data.created_at
    updated_at:str = raw_data.updated_at
    is_active:bool = raw_data.is_active

    header_authorization:str = request.headers.get('header-authorization')



    try:
        auth = jwt.decode(
            header_authorization,
            'o3xsO1FLiEjpWhrCnAPqFgJ0cRu4W1DCaOU_RbfbZ6ZbH6GyN9K7IwFbTzwDqKc5',
            algorithms=['HS256']
        )
    except jwt.ExpiredSignatureError:
        auth = 'Token has expired.'
    except jwt.InvalidTokenError:
        auth = 'Invalid token.'


    record_to_be_added = {'name': name, 'description': description}
    new_communities = models.Communities(**record_to_be_added)
    db.add(new_communities)
    db.commit()
    db.refresh(new_communities)
    communities_add_record = new_communities.to_dict()


    
    from datetime import datetime

    try:
        created_at: str = datetime.now().isoformat()
    except Exception as e:
        raise HTTPException(500, str(e))



    import uuid

    try:
        new_id = uuid.uuid4()
        print(new_id)
    except Exception as e:
        raise HTTPException(500, str(e))


    res = {
        'communities_add_record': communities_add_record,
        'auth': auth,
        'uuid': new_id,
    }
    return res

async def post_community_users(db: Session, raw_data: schemas.PostCommunityUsers):
    id:int = raw_data.id
    community_id:str = raw_data.community_id
    user_id:str = raw_data.user_id
    created_at:str = raw_data.created_at
    updated_at:str = raw_data.updated_at
    blocked:bool = raw_data.blocked


    record_to_be_added = {'id': id, 'blocked': blocked, 'user_id': user_id, 'created_at': created_at, 'updated_at': updated_at, 'community_id': community_id}
    new_community_users = models.CommunityUsers(**record_to_be_added)
    db.add(new_community_users)
    db.commit()
    db.refresh(new_community_users)
    community_users_inserted_record = new_community_users.to_dict()

    res = {
        'community_users_inserted_record': community_users_inserted_record,
    }
    return res

async def post_user(db: Session, raw_data: schemas.PostUser):
    name:str = raw_data.name
    email:str = raw_data.email
    phone:str = raw_data.phone
    country_code:str = raw_data.country_code
    gender:str = raw_data.gender
    user_avatar:str = raw_data.user_avatar
    password:str = raw_data.password
    streak:int = raw_data.streak
    is_blocked:bool = raw_data.is_blocked


    import uuid

    try:
        user_id: str = str(uuid.uuid4())
        print(f"user_id: {user_id}")
    except Exception as e:
        raise HTTPException(500, str(e))



    
    from datetime import datetime

    try:
        created_date:str = str(datetime.now())
        
        print(f"Created Date: {created_date}")
    except Exception as e:
        raise HTTPException(500, str(e))



    record_to_be_added = {'name': name, 'email': email, 'phone': phone, 'gender': gender, 'user_id': user_id, 'password': password, 'created_at': created_date, 'is_blocked': is_blocked, 'updated_at': created_date, 'country_code': country_code}
    new_user = models.User(**record_to_be_added)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    use_add_record = new_user.to_dict()



    bs_jwt_payload = {
        'exp': int((datetime.datetime.utcnow() + datetime.timedelta(seconds=100000)).timestamp()),
        'data': use_add_record
    }

    jwt = jwt.encode(bs_jwt_payload, 'o3xsO1FLiEjpWhrCnAPqFgJ0cRu4W1DCaOU_RbfbZ6ZbH6GyN9K7IwFbTzwDqKc5', algorithm='HS256')

    res = {
        'uuid_user_id': user_id,
        'updated_date': created_date,
        'user_add': use_add_record,
        'jwt': jwt,
    }
    return res

async def post_login(db: Session, raw_data: schemas.PostLogin):
    email:str = raw_data.email
    password:str = raw_data.password


    user_login = db.query(models.User).filter(models.User.email == email).first() 
    user_login = user_login.to_dict() if user_login else user_login



    bs_jwt_payload = {
        'exp': int((datetime.datetime.utcnow() + datetime.timedelta(seconds=200000)).timestamp()),
        'data': user_login
    }

    jwt_privete_login_keys = jwt.encode(bs_jwt_payload, 'o3xsO1FLiEjpWhrCnAPqFgJ0cRu4W1DCaOU_RbfbZ6ZbH6GyN9K7IwFbTzwDqKc5', algorithm='HS256')

    res = {
        'user_login': user_login,
        'jwt_private_key_login': jwt_privete_login_keys,
    }
    return res

async def get_communities(db: Session):

    communities_all = db.query(models.Communities).all()
    communities_all = [new_data.to_dict() for new_data in communities_all] if communities_all else communities_all

    res = {
        'communities_all': communities_all,
    }
    return res

async def get_date(db: Session):

    date_all = db.query(models.Date).all()
    date_all = [new_data.to_dict() for new_data in date_all] if date_all else date_all

    res = {
        'date_all': date_all,
    }
    return res

async def get_image(db: Session):

    image_all = db.query(models.Image).all()
    image_all = [new_data.to_dict() for new_data in image_all] if image_all else image_all

    res = {
        'image_all': image_all,
    }
    return res

async def get_image_id(db: Session, id: int):

    image_one = db.query(models.Image).filter(models.Image.id == id).first() 
    image_one = image_one.to_dict() if image_one else image_one

    res = {
        'image_one': image_one,
    }
    return res

async def post_image(db: Session, raw_data: schemas.PostImage):
    id:int = raw_data.id
    ratio:str = raw_data.ratio
    url:str = raw_data.url
    width:int = raw_data.width
    height:int = raw_data.height
    fallback:bool = raw_data.fallback
    event_id:uuid.UUID = raw_data.event_id


    record_to_be_added = {'id': id, 'url': url, 'ratio': ratio, 'width': width, 'height': height, 'event_id': event_id, 'fallback': fallback}
    new_image = models.Image(**record_to_be_added)
    db.add(new_image)
    db.commit()
    db.refresh(new_image)
    image_inserted_record = new_image.to_dict()

    res = {
        'image_inserted_record': image_inserted_record,
    }
    return res

async def put_image_id(db: Session, id: int, ratio: str, url: str, width: int, height: int, fallback: str, event_id: str):

    image_edited_record = db.query(models.Image).filter(models.Image.id == id).first()
    for key, value in {'id': id, 'url': url, 'ratio': ratio, 'width': width, 'height': height, 'event_id': event_id, 'fallback': fallback}.items():
          setattr(image_edited_record, key, value)
    db.commit()
    db.refresh(image_edited_record)
    image_edited_record = image_edited_record.to_dict() 

    res = {
        'image_edited_record': image_edited_record,
    }
    return res

async def delete_image_id(db: Session, id: int):

    image_deleted = None
    record_to_delete = db.query(models.Image).filter(models.Image.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        image_deleted = record_to_delete.to_dict() 

    res = {
        'image_deleted': image_deleted,
    }
    return res

async def get_event(db: Session):

    event_all = db.query(models.Event).all()
    event_all = [new_data.to_dict() for new_data in event_all] if event_all else event_all

    res = {
        'event_all': event_all,
    }
    return res

async def get_event_id(db: Session, id: int):

    event_one = db.query(models.Event).filter(models.Event.id == id).first() 
    event_one = event_one.to_dict() if event_one else event_one

    res = {
        'event_one': event_one,
    }
    return res

async def post_event(db: Session, raw_data: schemas.PostEvent):
    id:int = raw_data.id
    name:str = raw_data.name
    type:str = raw_data.type
    url:str = raw_data.url
    locale:str = raw_data.locale
    segment:str = raw_data.segment
    genre:str = raw_data.genre
    sub_genre:str = raw_data.sub_genre
    event_type:str = raw_data.event_type
    sub_type:str = raw_data.sub_type
    min_price:str = raw_data.min_price
    max_price:str = raw_data.max_price
    currency_type:str = raw_data.currency_type
    seatmap_url:str = raw_data.seatmap_url
    safe_tix:bool = raw_data.safe_tix
    min_age:int = raw_data.min_age
    ticket_limit:str = raw_data.ticket_limit
    accessibility_limit:str = raw_data.accessibility_limit
    all_inclusive_pricing:bool = raw_data.all_inclusive_pricing
    created_at:datetime.datetime = raw_data.created_at
    updated_at:datetime.datetime = raw_data.updated_at
    date_id:int = raw_data.date_id
    venue_id:int = raw_data.venue_id
    event_id:uuid.UUID = raw_data.event_id
    is_trending:bool = raw_data.is_trending
    is_active:bool = raw_data.is_active


    record_to_be_added = {'id': id, 'url': url, 'name': name, 'type': type, 'genre': genre, 'locale': locale, 'date_id': date_id, 'min_age': min_age, 'segment': segment, 'event_id': event_id, 'safe_tix': safe_tix, 'sub_type': sub_type, 'venue_id': venue_id, 'is_active': is_active, 'max_price': max_price, 'min_price': min_price, 'sub_genre': sub_genre, 'created_at': created_at, 'event_type': event_type, 'updated_at': updated_at, 'is_trending': is_trending, 'seatmap_url': seatmap_url, 'ticket_limit': ticket_limit, 'currency_type': currency_type, 'accessibility_limit': accessibility_limit, 'all_inclusive_pricing': all_inclusive_pricing}
    new_event = models.Event(**record_to_be_added)
    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    event_inserted_record = new_event.to_dict()

    res = {
        'event_inserted_record': event_inserted_record,
    }
    return res

async def put_event_id(db: Session, id: int, name: str, type: str, url: str, locale: str, segment: str, genre: str, sub_genre: str, event_type: str, sub_type: str, min_price: str, max_price: str, currency_type: str, seatmap_url: str, safe_tix: str, min_age: int, ticket_limit: str, accessibility_limit: str, all_inclusive_pricing: str, created_at: str, updated_at: str, date_id: int, venue_id: int, event_id: str, is_trending: str, is_active: str):

    event_edited_record = db.query(models.Event).filter(models.Event.id == id).first()
    for key, value in {'id': id, 'url': url, 'name': name, 'type': type, 'genre': genre, 'locale': locale, 'date_id': date_id, 'min_age': min_age, 'segment': segment, 'event_id': event_id, 'safe_tix': safe_tix, 'sub_type': sub_type, 'venue_id': venue_id, 'is_active': is_active, 'max_price': max_price, 'min_price': min_price, 'sub_genre': sub_genre, 'created_at': created_at, 'event_type': event_type, 'updated_at': updated_at, 'is_trending': is_trending, 'seatmap_url': seatmap_url, 'ticket_limit': ticket_limit, 'currency_type': currency_type, 'accessibility_limit': accessibility_limit, 'all_inclusive_pricing': all_inclusive_pricing}.items():
          setattr(event_edited_record, key, value)
    db.commit()
    db.refresh(event_edited_record)
    event_edited_record = event_edited_record.to_dict() 

    res = {
        'event_edited_record': event_edited_record,
    }
    return res

async def delete_event_id(db: Session, id: int):

    event_deleted = None
    record_to_delete = db.query(models.Event).filter(models.Event.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        event_deleted = record_to_delete.to_dict() 

    res = {
        'event_deleted': event_deleted,
    }
    return res

async def get_date_id(db: Session, id: int):

    date_one = db.query(models.Date).filter(models.Date.id == id).first() 
    date_one = date_one.to_dict() if date_one else date_one

    res = {
        'date_one': date_one,
    }
    return res

async def post_date(db: Session, raw_data: schemas.PostDate):
    id:int = raw_data.id
    timezone:str = raw_data.timezone
    status:str = raw_data.status
    span_multiple_days:bool = raw_data.span_multiple_days
    local_date:str = raw_data.local_date
    local_time:str = raw_data.local_time
    datetime:datetime.datetime = raw_data.datetime
    date_tbd:bool = raw_data.date_tbd
    date_tba:bool = raw_data.date_tba
    time_tba:bool = raw_data.time_tba
    no_specific_time:bool = raw_data.no_specific_time


    record_to_be_added = {'id': id, 'status': status, 'date_tba': date_tba, 'date_tbd': date_tbd, 'datetime': datetime, 'time_tba': time_tba, 'timezone': timezone, 'local_date': local_date, 'local_time': local_time, 'no_specific_time': no_specific_time, 'span_multiple_days': span_multiple_days}
    new_date = models.Date(**record_to_be_added)
    db.add(new_date)
    db.commit()
    db.refresh(new_date)
    date_inserted_record = new_date.to_dict()

    res = {
        'date_inserted_record': date_inserted_record,
    }
    return res

async def put_date_id(db: Session, id: int, timezone: str, status: str, span_multiple_days: str, local_date: str, local_time: str, datetime: str, date_tbd: str, date_tba: str, time_tba: str, no_specific_time: str):

    date_edited_record = db.query(models.Date).filter(models.Date.id == id).first()
    for key, value in {'id': id, 'status': status, 'date_tba': date_tba, 'date_tbd': date_tbd, 'datetime': datetime, 'time_tba': time_tba, 'timezone': timezone, 'local_date': local_date, 'local_time': local_time, 'no_specific_time': no_specific_time, 'span_multiple_days': span_multiple_days}.items():
          setattr(date_edited_record, key, value)
    db.commit()
    db.refresh(date_edited_record)
    date_edited_record = date_edited_record.to_dict() 

    res = {
        'date_edited_record': date_edited_record,
    }
    return res

async def delete_date_id(db: Session, id: int):

    date_deleted = None
    record_to_delete = db.query(models.Date).filter(models.Date.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        date_deleted = record_to_delete.to_dict() 

    res = {
        'date_deleted': date_deleted,
    }
    return res

async def get_venue(db: Session):

    venue_all = db.query(models.Venue).all()
    venue_all = [new_data.to_dict() for new_data in venue_all] if venue_all else venue_all

    res = {
        'venue_all': venue_all,
    }
    return res

async def get_venue_id(db: Session, id: int):

    venue_one = db.query(models.Venue).filter(models.Venue.id == id).first() 
    venue_one = venue_one.to_dict() if venue_one else venue_one

    res = {
        'venue_one': venue_one,
    }
    return res

async def delete_posts_id(db: Session, id: int):

    posts_deleted = None
    record_to_delete = db.query(models.Posts).filter(models.Posts.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        posts_deleted = record_to_delete.to_dict() 

    res = {
        'posts_deleted': posts_deleted,
    }
    return res

async def post_venue(db: Session, raw_data: schemas.PostVenue):
    id:int = raw_data.id
    name:str = raw_data.name
    type:str = raw_data.type
    url:str = raw_data.url
    locale:str = raw_data.locale
    postal_code:str = raw_data.postal_code
    timezone:str = raw_data.timezone
    city:str = raw_data.city
    state:str = raw_data.state
    country:str = raw_data.country
    country_code:str = raw_data.country_code
    address_line1:str = raw_data.address_line1
    longitude:float = raw_data.longitude
    latitude:float = raw_data.latitude
    phone_number_detail:str = raw_data.phone_number_detail
    open_hours_detail:str = raw_data.open_hours_detail
    accepted_payment_detail:str = raw_data.accepted_payment_detail
    will_call_detail:str = raw_data.will_call_detail
    created_at:datetime.datetime = raw_data.created_at
    updated_at:datetime.datetime = raw_data.updated_at


    record_to_be_added = {'id': id, 'url': url, 'city': city, 'name': name, 'type': type, 'state': state, 'locale': locale, 'country': country, 'latitude': latitude, 'timezone': timezone, 'longitude': longitude, 'created_at': created_at, 'updated_at': updated_at, 'postal_code': postal_code, 'country_code': country_code, 'address_line1': address_line1, 'will_call_detail': will_call_detail, 'open_hours_detail': open_hours_detail, 'phone_number_detail': phone_number_detail, 'accepted_payment_detail': accepted_payment_detail}
    new_venue = models.Venue(**record_to_be_added)
    db.add(new_venue)
    db.commit()
    db.refresh(new_venue)
    venue_inserted_record = new_venue.to_dict()

    res = {
        'venue_inserted_record': venue_inserted_record,
    }
    return res

async def put_venue_id(db: Session, id: int, name: str, type: str, url: str, locale: str, postal_code: str, timezone: str, city: str, state: str, country: str, country_code: str, address_line1: str, longitude: float, latitude: float, phone_number_detail: str, open_hours_detail: str, accepted_payment_detail: str, will_call_detail: str, created_at: str, updated_at: str):

    venue_edited_record = db.query(models.Venue).filter(models.Venue.id == id).first()
    for key, value in {'id': id, 'url': url, 'city': city, 'name': name, 'type': type, 'state': state, 'locale': locale, 'country': country, 'latitude': latitude, 'timezone': timezone, 'longitude': longitude, 'created_at': created_at, 'updated_at': updated_at, 'postal_code': postal_code, 'country_code': country_code, 'address_line1': address_line1, 'will_call_detail': will_call_detail, 'open_hours_detail': open_hours_detail, 'phone_number_detail': phone_number_detail, 'accepted_payment_detail': accepted_payment_detail}.items():
          setattr(venue_edited_record, key, value)
    db.commit()
    db.refresh(venue_edited_record)
    venue_edited_record = venue_edited_record.to_dict() 

    res = {
        'venue_edited_record': venue_edited_record,
    }
    return res

async def delete_venue_id(db: Session, id: int):

    venue_deleted = None
    record_to_delete = db.query(models.Venue).filter(models.Venue.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        venue_deleted = record_to_delete.to_dict() 

    res = {
        'venue_deleted': venue_deleted,
    }
    return res

async def get_posts_like(db: Session):

    posts_like_all = db.query(models.PostsLike).all()
    posts_like_all = [new_data.to_dict() for new_data in posts_like_all] if posts_like_all else posts_like_all

    res = {
        'posts_like_all': posts_like_all,
    }
    return res

async def get_posts_like_id(db: Session, id: int):

    posts_like_one = db.query(models.PostsLike).filter(models.PostsLike.id == id).first() 
    posts_like_one = posts_like_one.to_dict() if posts_like_one else posts_like_one

    res = {
        'posts_like_one': posts_like_one,
    }
    return res

async def post_posts_like(db: Session, raw_data: schemas.PostPostsLike):
    id:int = raw_data.id
    user_id:uuid.UUID = raw_data.user_id
    post_id:uuid.UUID = raw_data.post_id
    reaction_alias:str = raw_data.reaction_alias


    record_to_be_added = {'id': id, 'post_id': post_id, 'user_id': user_id, 'reaction_alias': reaction_alias}
    new_posts_like = models.PostsLike(**record_to_be_added)
    db.add(new_posts_like)
    db.commit()
    db.refresh(new_posts_like)
    posts_like_inserted_record = new_posts_like.to_dict()

    res = {
        'posts_like_inserted_record': posts_like_inserted_record,
    }
    return res

async def put_posts_like_id(db: Session, id: int, user_id: str, post_id: str, reaction_alias: str):

    posts_like_edited_record = db.query(models.PostsLike).filter(models.PostsLike.id == id).first()
    for key, value in {'id': id, 'post_id': post_id, 'user_id': user_id, 'reaction_alias': reaction_alias}.items():
          setattr(posts_like_edited_record, key, value)
    db.commit()
    db.refresh(posts_like_edited_record)
    posts_like_edited_record = posts_like_edited_record.to_dict() 

    res = {
        'posts_like_edited_record': posts_like_edited_record,
    }
    return res

async def delete_posts_like_id(db: Session, id: int):

    posts_like_deleted = None
    record_to_delete = db.query(models.PostsLike).filter(models.PostsLike.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        posts_like_deleted = record_to_delete.to_dict() 

    res = {
        'posts_like_deleted': posts_like_deleted,
    }
    return res

async def get_posts(db: Session):

    posts_all = db.query(models.Posts).all()
    posts_all = [new_data.to_dict() for new_data in posts_all] if posts_all else posts_all

    res = {
        'posts_all': posts_all,
    }
    return res

async def get_posts_id(db: Session, id: int):

    posts_one = db.query(models.Posts).filter(models.Posts.id == id).first() 
    posts_one = posts_one.to_dict() if posts_one else posts_one

    res = {
        'posts_one': posts_one,
    }
    return res

async def post_posts(db: Session, raw_data: schemas.PostPosts):
    id:int = raw_data.id
    post_id:uuid.UUID = raw_data.post_id
    community_id:uuid.UUID = raw_data.community_id
    user_id:uuid.UUID = raw_data.user_id
    caption:str = raw_data.caption
    image:str = raw_data.image
    status_alias:str = raw_data.status_alias
    created_at:datetime.datetime = raw_data.created_at
    updated_at:datetime.datetime = raw_data.updated_at
    post_type:str = raw_data.post_type
    ref_event_id:str = raw_data.ref_event_id


    record_to_be_added = {'id': id, 'image': image, 'caption': caption, 'post_id': post_id, 'user_id': user_id, 'post_type': post_type, 'created_at': created_at, 'updated_at': updated_at, 'community_id': community_id, 'ref_event_id': ref_event_id, 'status_alias': status_alias}
    new_posts = models.Posts(**record_to_be_added)
    db.add(new_posts)
    db.commit()
    db.refresh(new_posts)
    posts_inserted_record = new_posts.to_dict()

    res = {
        'posts_inserted_record': posts_inserted_record,
    }
    return res

async def put_posts_id(db: Session, id: int, post_id: str, community_id: str, user_id: str, caption: str, image: str, status_alias: str, created_at: str, updated_at: str, post_type: str, ref_event_id: str):

    posts_edited_record = db.query(models.Posts).filter(models.Posts.id == id).first()
    for key, value in {'id': id, 'image': image, 'caption': caption, 'post_id': post_id, 'user_id': user_id, 'post_type': post_type, 'created_at': created_at, 'updated_at': updated_at, 'community_id': community_id, 'ref_event_id': ref_event_id, 'status_alias': status_alias}.items():
          setattr(posts_edited_record, key, value)
    db.commit()
    db.refresh(posts_edited_record)
    posts_edited_record = posts_edited_record.to_dict() 

    res = {
        'posts_edited_record': posts_edited_record,
    }
    return res

async def get_communities_id(db: Session, id: int):

    communities_one = db.query(models.Communities).filter(models.Communities.id == id).first() 
    communities_one = communities_one.to_dict() if communities_one else communities_one

    res = {
        'communities_one': communities_one,
    }
    return res

async def put_communities_id(db: Session, id: int, community_id: str, name: str, description: str, image: str, category: str, type: str, admin_id: str, status_alias: str, created_at: str, updated_at: str, is_active: str):

    communities_edited_record = db.query(models.Communities).filter(models.Communities.id == id).first()
    for key, value in {'id': id, 'name': name, 'type': type, 'image': image, 'admin_id': admin_id, 'category': category, 'is_active': is_active, 'created_at': created_at, 'updated_at': updated_at, 'description': description, 'community_id': community_id, 'status_alias': status_alias}.items():
          setattr(communities_edited_record, key, value)
    db.commit()
    db.refresh(communities_edited_record)
    communities_edited_record = communities_edited_record.to_dict() 

    res = {
        'communities_edited_record': communities_edited_record,
    }
    return res

async def delete_communities_id(db: Session, id: int):

    communities_deleted = None
    record_to_delete = db.query(models.Communities).filter(models.Communities.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        communities_deleted = record_to_delete.to_dict() 

    res = {
        'communities_deleted': communities_deleted,
    }
    return res

async def get_user(db: Session):

    user_all = db.query(models.User).all()
    user_all = [new_data.to_dict() for new_data in user_all] if user_all else user_all

    res = {
        'user_all': user_all,
    }
    return res

async def get_user_user_id(db: Session, user_id: int):

    user_one = db.query(models.User).filter(models.User.user_id == user_id).first() 
    user_one = user_one.to_dict() if user_one else user_one

    res = {
        'user_one': user_one,
    }
    return res

async def put_user_user_id(db: Session, user_id: str, name: str, email: str, phone: str, country_code: str, login_type: str, google_id: str, apple_id: str, created_at: str, updated_at: str, gender: str, id: int, streak: int, last_login: str, user_avatar: str, is_blocked: str):

    user_edited_record = db.query(models.User).filter(models.User.user_id == user_id).first()
    for key, value in {'id': id, 'name': name, 'email': email, 'phone': phone, 'gender': gender, 'streak': streak, 'user_id': user_id, 'apple_id': apple_id, 'google_id': google_id, 'created_at': created_at, 'is_blocked': is_blocked, 'last_login': last_login, 'login_type': login_type, 'updated_at': updated_at, 'user_avatar': user_avatar, 'country_code': country_code}.items():
          setattr(user_edited_record, key, value)
    db.commit()
    db.refresh(user_edited_record)
    user_edited_record = user_edited_record.to_dict() 

    res = {
        'user_edited_record': user_edited_record,
    }
    return res

async def delete_user_user_id(db: Session, user_id: int):

    user_deleted = None
    record_to_delete = db.query(models.User).filter(models.User.user_id == user_id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        user_deleted = record_to_delete.to_dict() 

    res = {
        'user_deleted': user_deleted,
    }
    return res

async def get_attraction(db: Session):

    attraction_all = db.query(models.Attraction).all()
    attraction_all = [new_data.to_dict() for new_data in attraction_all] if attraction_all else attraction_all

    res = {
        'attraction_all': attraction_all,
    }
    return res

async def get_attraction_id(db: Session, id: int):

    attraction_one = db.query(models.Attraction).filter(models.Attraction.id == id).first() 
    attraction_one = attraction_one.to_dict() if attraction_one else attraction_one

    res = {
        'attraction_one': attraction_one,
    }
    return res

async def post_crm_users(db: Session, raw_data: schemas.PostCrmUsers , request: Request):
    id:int = raw_data.id
    crm_id:uuid.UUID = raw_data.crm_id
    name:str = raw_data.name
    email:str = raw_data.email
    password:str = raw_data.password
    recovery_number:str = raw_data.recovery_number
    designation:str = raw_data.designation
    department:str = raw_data.department
    role:str = raw_data.role
    created_at:datetime.datetime = raw_data.created_at
    updated_at:datetime.datetime = raw_data.updated_at
    is_blocked:bool = raw_data.is_blocked

    header_authorization:str = request.headers.get('header-authorization')


    record_to_be_added = {'id': id, 'name': name, 'role': role, 'email': email, 'crm_id': crm_id, 'password': password, 'created_at': created_at, 'department': department, 'is_blocked': is_blocked, 'updated_at': updated_at, 'designation': designation, 'recovery_number': recovery_number}
    new_crm_users = models.CrmUsers(**record_to_be_added)
    db.add(new_crm_users)
    db.commit()
    db.refresh(new_crm_users)
    crm_users_inserted_record = new_crm_users.to_dict()

    res = {
        'crm_users_inserted_record': crm_users_inserted_record,
    }
    return res

async def put_attraction_id(db: Session, id: int, name: str, url: str, event_id: str):

    attraction_edited_record = db.query(models.Attraction).filter(models.Attraction.id == id).first()
    for key, value in {'id': id, 'url': url, 'name': name, 'event_id': event_id}.items():
          setattr(attraction_edited_record, key, value)
    db.commit()
    db.refresh(attraction_edited_record)
    attraction_edited_record = attraction_edited_record.to_dict() 

    res = {
        'attraction_edited_record': attraction_edited_record,
    }
    return res

async def delete_attraction_id(db: Session, id: int):

    attraction_deleted = None
    record_to_delete = db.query(models.Attraction).filter(models.Attraction.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        attraction_deleted = record_to_delete.to_dict() 

    res = {
        'attraction_deleted': attraction_deleted,
    }
    return res

async def get_crm_users(db: Session):

    crm_users_all = db.query(models.CrmUsers).all()
    crm_users_all = [new_data.to_dict() for new_data in crm_users_all] if crm_users_all else crm_users_all

    res = {
        'crm_users_all': crm_users_all,
    }
    return res

async def get_crm_users_id(db: Session, id: int):

    crm_users_one = db.query(models.CrmUsers).filter(models.CrmUsers.id == id).first() 
    crm_users_one = crm_users_one.to_dict() if crm_users_one else crm_users_one

    res = {
        'crm_users_one': crm_users_one,
    }
    return res

async def delete_reward_id(db: Session, id: int):

    reward_deleted = None
    record_to_delete = db.query(models.Reward).filter(models.Reward.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        reward_deleted = record_to_delete.to_dict() 

    res = {
        'reward_deleted': reward_deleted,
    }
    return res

async def put_crm_users_id(db: Session, id: int, crm_id: str, name: str, email: str, password: str, recovery_number: str, designation: str, department: str, role: str, created_at: str, updated_at: str, is_blocked: str):

    crm_users_edited_record = db.query(models.CrmUsers).filter(models.CrmUsers.id == id).first()
    for key, value in {'id': id, 'name': name, 'role': role, 'email': email, 'crm_id': crm_id, 'password': password, 'created_at': created_at, 'department': department, 'is_blocked': is_blocked, 'updated_at': updated_at, 'designation': designation, 'recovery_number': recovery_number}.items():
          setattr(crm_users_edited_record, key, value)
    db.commit()
    db.refresh(crm_users_edited_record)
    crm_users_edited_record = crm_users_edited_record.to_dict() 

    res = {
        'crm_users_edited_record': crm_users_edited_record,
    }
    return res

async def delete_crm_users_id(db: Session, id: int):

    crm_users_deleted = None
    record_to_delete = db.query(models.CrmUsers).filter(models.CrmUsers.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        crm_users_deleted = record_to_delete.to_dict() 

    res = {
        'crm_users_deleted': crm_users_deleted,
    }
    return res

async def get_reward(db: Session):

    reward_all = db.query(models.Reward).all()
    reward_all = [new_data.to_dict() for new_data in reward_all] if reward_all else reward_all

    res = {
        'reward_all': reward_all,
    }
    return res

async def get_reward_id(db: Session, id: int):

    reward_one = db.query(models.Reward).filter(models.Reward.id == id).first() 
    reward_one = reward_one.to_dict() if reward_one else reward_one

    res = {
        'reward_one': reward_one,
    }
    return res

async def post_reward(db: Session, raw_data: schemas.PostReward):
    id:int = raw_data.id
    reward_id:uuid.UUID = raw_data.reward_id
    name:str = raw_data.name
    alias:str = raw_data.alias
    reward_on:str = raw_data.reward_on
    value:str = raw_data.value
    frequency:int = raw_data.frequency
    img_url:str = raw_data.img_url
    creted_at:datetime.datetime = raw_data.creted_at
    updated_at:datetime.datetime = raw_data.updated_at
    reward_type:str = raw_data.reward_type
    earn_bonus:str = raw_data.earn_bonus
    sub_description:str = raw_data.sub_description
    is_active:bool = raw_data.is_active


    record_to_be_added = {'id': id, 'name': name, 'alias': alias, 'value': value, 'img_url': img_url, 'creted_at': creted_at, 'frequency': frequency, 'is_active': is_active, 'reward_id': reward_id, 'reward_on': reward_on, 'earn_bonus': earn_bonus, 'updated_at': updated_at, 'reward_type': reward_type, 'sub_description': sub_description}
    new_reward = models.Reward(**record_to_be_added)
    db.add(new_reward)
    db.commit()
    db.refresh(new_reward)
    reward_inserted_record = new_reward.to_dict()

    res = {
        'reward_inserted_record': reward_inserted_record,
    }
    return res

async def put_reward_id(db: Session, id: int, reward_id: str, name: str, alias: str, reward_on: str, value: str, frequency: int, img_url: str, creted_at: str, updated_at: str, reward_type: str, earn_bonus: str, sub_description: str, is_active: str):

    reward_edited_record = db.query(models.Reward).filter(models.Reward.id == id).first()
    for key, value in {'id': id, 'name': name, 'alias': alias, 'value': value, 'img_url': img_url, 'creted_at': creted_at, 'frequency': frequency, 'is_active': is_active, 'reward_id': reward_id, 'reward_on': reward_on, 'earn_bonus': earn_bonus, 'updated_at': updated_at, 'reward_type': reward_type, 'sub_description': sub_description}.items():
          setattr(reward_edited_record, key, value)
    db.commit()
    db.refresh(reward_edited_record)
    reward_edited_record = reward_edited_record.to_dict() 

    res = {
        'reward_edited_record': reward_edited_record,
    }
    return res

async def get_question_master(db: Session):

    question_master_all = db.query(models.QuestionMaster).all()
    question_master_all = [new_data.to_dict() for new_data in question_master_all] if question_master_all else question_master_all

    res = {
        'question_master_all': question_master_all,
    }
    return res

async def get_question_master_id(db: Session, id: int):

    question_master_one = db.query(models.QuestionMaster).filter(models.QuestionMaster.id == id).first() 
    question_master_one = question_master_one.to_dict() if question_master_one else question_master_one

    res = {
        'question_master_one': question_master_one,
    }
    return res

async def post_question_master(db: Session, raw_data: schemas.PostQuestionMaster):
    type:str = raw_data.type
    question:str = raw_data.question
    status:str = raw_data.status
    created_at:datetime.datetime = raw_data.created_at
    updated_at:datetime.datetime = raw_data.updated_at
    created_by:str = raw_data.created_by
    updated_by:str = raw_data.updated_by
    is_active:bool = raw_data.is_active
    min_range:int = raw_data.min_range
    max_range:int = raw_data.max_range
    id:int = raw_data.id


    record_to_be_added = {'id': id, 'type': type, 'status': status, 'question': question, 'is_active': is_active, 'max_range': max_range, 'min_range': min_range, 'created_at': created_at, 'created_by': created_by, 'updated_at': updated_at, 'updated_by': updated_by}
    new_question_master = models.QuestionMaster(**record_to_be_added)
    db.add(new_question_master)
    db.commit()
    db.refresh(new_question_master)
    question_master_inserted_record = new_question_master.to_dict()

    res = {
        'question_master_inserted_record': question_master_inserted_record,
    }
    return res

async def put_question_master_id(db: Session, type: str, question: str, status: str, created_at: str, updated_at: str, created_by: str, updated_by: str, is_active: str, min_range: int, max_range: int, id: int):

    question_master_edited_record = db.query(models.QuestionMaster).filter(models.QuestionMaster.id == id).first()
    for key, value in {'id': id, 'type': type, 'status': status, 'question': question, 'is_active': is_active, 'max_range': max_range, 'min_range': min_range, 'created_at': created_at, 'created_by': created_by, 'updated_at': updated_at, 'updated_by': updated_by}.items():
          setattr(question_master_edited_record, key, value)
    db.commit()
    db.refresh(question_master_edited_record)
    question_master_edited_record = question_master_edited_record.to_dict() 

    res = {
        'question_master_edited_record': question_master_edited_record,
    }
    return res

async def delete_question_master_id(db: Session, id: int):

    question_master_deleted = None
    record_to_delete = db.query(models.QuestionMaster).filter(models.QuestionMaster.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        question_master_deleted = record_to_delete.to_dict() 

    res = {
        'question_master_deleted': question_master_deleted,
    }
    return res

async def get_user_sessions(db: Session):

    user_sessions_all = db.query(models.UserSessions).all()
    user_sessions_all = [new_data.to_dict() for new_data in user_sessions_all] if user_sessions_all else user_sessions_all

    res = {
        'user_sessions_all': user_sessions_all,
    }
    return res

async def get_community_users(db: Session):

    community_users_all = db.query(models.CommunityUsers).all()
    community_users_all = [new_data.to_dict() for new_data in community_users_all] if community_users_all else community_users_all

    res = {
        'community_users_all': community_users_all,
    }
    return res

async def get_user_sessions_session_id(db: Session, session_id: int):

    user_sessions_one = db.query(models.UserSessions).filter(models.UserSessions.session_id == session_id).first() 
    user_sessions_one = user_sessions_one.to_dict() if user_sessions_one else user_sessions_one

    res = {
        'user_sessions_one': user_sessions_one,
    }
    return res

async def post_user_sessions(db: Session, raw_data: schemas.PostUserSessions):
    session_id:str = raw_data.session_id
    user_id:uuid.UUID = raw_data.user_id
    device_type:str = raw_data.device_type
    device_id:str = raw_data.device_id
    app_version:str = raw_data.app_version
    os_version:str = raw_data.os_version
    access_token:str = raw_data.access_token
    refresh_token:str = raw_data.refresh_token
    ip_address:str = raw_data.ip_address
    user_agent:str = raw_data.user_agent
    location:str = raw_data.location
    login_time:datetime.datetime = raw_data.login_time
    last_activity:datetime.datetime = raw_data.last_activity
    expiration_time:datetime.datetime = raw_data.expiration_time
    status:str = raw_data.status
    created_at:datetime.datetime = raw_data.created_at
    updated_at:datetime.datetime = raw_data.updated_at


    record_to_be_added = {'status': status, 'user_id': user_id, 'location': location, 'device_id': device_id, 'created_at': created_at, 'ip_address': ip_address, 'login_time': login_time, 'os_version': os_version, 'session_id': session_id, 'updated_at': updated_at, 'user_agent': user_agent, 'app_version': app_version, 'device_type': device_type, 'access_token': access_token, 'last_activity': last_activity, 'refresh_token': refresh_token, 'expiration_time': expiration_time}
    new_user_sessions = models.UserSessions(**record_to_be_added)
    db.add(new_user_sessions)
    db.commit()
    db.refresh(new_user_sessions)
    user_sessions_inserted_record = new_user_sessions.to_dict()

    res = {
        'user_sessions_inserted_record': user_sessions_inserted_record,
    }
    return res

async def put_user_sessions_session_id(db: Session, session_id: str, user_id: str, device_type: str, device_id: str, app_version: str, os_version: str, access_token: str, refresh_token: str, ip_address: str, user_agent: str, location: str, login_time: str, last_activity: str, expiration_time: str, status: str, created_at: str, updated_at: str):

    user_sessions_edited_record = db.query(models.UserSessions).filter(models.UserSessions.session_id == session_id).first()
    for key, value in {'status': status, 'user_id': user_id, 'location': location, 'device_id': device_id, 'created_at': created_at, 'ip_address': ip_address, 'login_time': login_time, 'os_version': os_version, 'session_id': session_id, 'updated_at': updated_at, 'user_agent': user_agent, 'app_version': app_version, 'device_type': device_type, 'access_token': access_token, 'last_activity': last_activity, 'refresh_token': refresh_token, 'expiration_time': expiration_time}.items():
          setattr(user_sessions_edited_record, key, value)
    db.commit()
    db.refresh(user_sessions_edited_record)
    user_sessions_edited_record = user_sessions_edited_record.to_dict() 

    res = {
        'user_sessions_edited_record': user_sessions_edited_record,
    }
    return res

async def delete_user_sessions_session_id(db: Session, session_id: int):

    user_sessions_deleted = None
    record_to_delete = db.query(models.UserSessions).filter(models.UserSessions.session_id == session_id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        user_sessions_deleted = record_to_delete.to_dict() 

    res = {
        'user_sessions_deleted': user_sessions_deleted,
    }
    return res

async def get_user_bucketlist(db: Session):

    user_bucketlist_all = db.query(models.UserBucketlist).all()
    user_bucketlist_all = [new_data.to_dict() for new_data in user_bucketlist_all] if user_bucketlist_all else user_bucketlist_all

    res = {
        'user_bucketlist_all': user_bucketlist_all,
    }
    return res

async def get_user_bucketlist_id(db: Session, id: int):

    user_bucketlist_one = db.query(models.UserBucketlist).filter(models.UserBucketlist.id == id).first() 
    user_bucketlist_one = user_bucketlist_one.to_dict() if user_bucketlist_one else user_bucketlist_one

    res = {
        'user_bucketlist_one': user_bucketlist_one,
    }
    return res

async def post_user_bucketlist(db: Session, raw_data: schemas.PostUserBucketlist):
    user_id:uuid.UUID = raw_data.user_id
    event_id:uuid.UUID = raw_data.event_id
    has_booked:bool = raw_data.has_booked
    booked_time:datetime.datetime = raw_data.booked_time
    created_at:datetime.datetime = raw_data.created_at
    id:int = raw_data.id


    record_to_be_added = {'id': id, 'user_id': user_id, 'event_id': event_id, 'created_at': created_at, 'has_booked': has_booked, 'booked_time': booked_time}
    new_user_bucketlist = models.UserBucketlist(**record_to_be_added)
    db.add(new_user_bucketlist)
    db.commit()
    db.refresh(new_user_bucketlist)
    user_bucketlist_inserted_record = new_user_bucketlist.to_dict()

    res = {
        'user_bucketlist_inserted_record': user_bucketlist_inserted_record,
    }
    return res

async def put_user_bucketlist_id(db: Session, user_id: str, event_id: str, has_booked: str, booked_time: str, created_at: str, id: int):

    user_bucketlist_edited_record = db.query(models.UserBucketlist).filter(models.UserBucketlist.id == id).first()
    for key, value in {'id': id, 'user_id': user_id, 'event_id': event_id, 'created_at': created_at, 'has_booked': has_booked, 'booked_time': booked_time}.items():
          setattr(user_bucketlist_edited_record, key, value)
    db.commit()
    db.refresh(user_bucketlist_edited_record)
    user_bucketlist_edited_record = user_bucketlist_edited_record.to_dict() 

    res = {
        'user_bucketlist_edited_record': user_bucketlist_edited_record,
    }
    return res

async def delete_user_bucketlist_id(db: Session, id: int):

    user_bucketlist_deleted = None
    record_to_delete = db.query(models.UserBucketlist).filter(models.UserBucketlist.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        user_bucketlist_deleted = record_to_delete.to_dict() 

    res = {
        'user_bucketlist_deleted': user_bucketlist_deleted,
    }
    return res

async def get_user_survey(db: Session):

    user_survey_all = db.query(models.UserSurvey).all()
    user_survey_all = [new_data.to_dict() for new_data in user_survey_all] if user_survey_all else user_survey_all

    res = {
        'user_survey_all': user_survey_all,
    }
    return res

async def get_user_survey_id(db: Session, id: int):

    user_survey_one = db.query(models.UserSurvey).filter(models.UserSurvey.id == id).first() 
    user_survey_one = user_survey_one.to_dict() if user_survey_one else user_survey_one

    res = {
        'user_survey_one': user_survey_one,
    }
    return res

async def post_user_survey(db: Session, raw_data: schemas.PostUserSurvey):
    created_at:datetime.datetime = raw_data.created_at
    updated_at:datetime.datetime = raw_data.updated_at
    user_id:uuid.UUID = raw_data.user_id
    id:int = raw_data.id
    question_id:int = raw_data.question_id
    answer_id:int = raw_data.answer_id


    record_to_be_added = {'id': id, 'user_id': user_id, 'answer_id': answer_id, 'created_at': created_at, 'updated_at': updated_at, 'question_id': question_id}
    new_user_survey = models.UserSurvey(**record_to_be_added)
    db.add(new_user_survey)
    db.commit()
    db.refresh(new_user_survey)
    user_survey_inserted_record = new_user_survey.to_dict()

    res = {
        'user_survey_inserted_record': user_survey_inserted_record,
    }
    return res

async def put_user_survey_id(db: Session, created_at: str, updated_at: str, user_id: str, id: int, question_id: int, answer_id: int):

    user_survey_edited_record = db.query(models.UserSurvey).filter(models.UserSurvey.id == id).first()
    for key, value in {'id': id, 'user_id': user_id, 'answer_id': answer_id, 'created_at': created_at, 'updated_at': updated_at, 'question_id': question_id}.items():
          setattr(user_survey_edited_record, key, value)
    db.commit()
    db.refresh(user_survey_edited_record)
    user_survey_edited_record = user_survey_edited_record.to_dict() 

    res = {
        'user_survey_edited_record': user_survey_edited_record,
    }
    return res

async def delete_user_survey_id(db: Session, id: int):

    user_survey_deleted = None
    record_to_delete = db.query(models.UserSurvey).filter(models.UserSurvey.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        user_survey_deleted = record_to_delete.to_dict() 

    res = {
        'user_survey_deleted': user_survey_deleted,
    }
    return res

async def get_user_reward(db: Session):

    user_reward_all = db.query(models.UserReward).all()
    user_reward_all = [new_data.to_dict() for new_data in user_reward_all] if user_reward_all else user_reward_all

    res = {
        'user_reward_all': user_reward_all,
    }
    return res

async def get_user_reward_id(db: Session, id: int):

    user_reward_one = db.query(models.UserReward).filter(models.UserReward.id == id).first() 
    user_reward_one = user_reward_one.to_dict() if user_reward_one else user_reward_one

    res = {
        'user_reward_one': user_reward_one,
    }
    return res

async def post_user_reward(db: Session, raw_data: schemas.PostUserReward):
    id:int = raw_data.id
    user_id:uuid.UUID = raw_data.user_id
    reward_id:uuid.UUID = raw_data.reward_id
    reward_value:int = raw_data.reward_value
    creted_at:datetime.datetime = raw_data.creted_at
    updated_at:datetime.datetime = raw_data.updated_at
    is_visible:bool = raw_data.is_visible


    record_to_be_added = {'id': id, 'user_id': user_id, 'creted_at': creted_at, 'reward_id': reward_id, 'is_visible': is_visible, 'updated_at': updated_at, 'reward_value': reward_value}
    new_user_reward = models.UserReward(**record_to_be_added)
    db.add(new_user_reward)
    db.commit()
    db.refresh(new_user_reward)
    user_reward_inserted_record = new_user_reward.to_dict()

    res = {
        'user_reward_inserted_record': user_reward_inserted_record,
    }
    return res

async def put_user_reward_id(db: Session, id: int, user_id: str, reward_id: str, reward_value: int, creted_at: str, updated_at: str, is_visible: str):

    user_reward_edited_record = db.query(models.UserReward).filter(models.UserReward.id == id).first()
    for key, value in {'id': id, 'user_id': user_id, 'creted_at': creted_at, 'reward_id': reward_id, 'is_visible': is_visible, 'updated_at': updated_at, 'reward_value': reward_value}.items():
          setattr(user_reward_edited_record, key, value)
    db.commit()
    db.refresh(user_reward_edited_record)
    user_reward_edited_record = user_reward_edited_record.to_dict() 

    res = {
        'user_reward_edited_record': user_reward_edited_record,
    }
    return res

async def delete_user_reward_id(db: Session, id: int):

    user_reward_deleted = None
    record_to_delete = db.query(models.UserReward).filter(models.UserReward.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        user_reward_deleted = record_to_delete.to_dict() 

    res = {
        'user_reward_deleted': user_reward_deleted,
    }
    return res

async def get_user_events(db: Session):

    user_events_all = db.query(models.UserEvents).all()
    user_events_all = [new_data.to_dict() for new_data in user_events_all] if user_events_all else user_events_all

    res = {
        'user_events_all': user_events_all,
    }
    return res

async def get_user_events_id(db: Session, id: int):

    user_events_one = db.query(models.UserEvents).filter(models.UserEvents.id == id).first() 
    user_events_one = user_events_one.to_dict() if user_events_one else user_events_one

    res = {
        'user_events_one': user_events_one,
    }
    return res

async def post_user_events(db: Session, raw_data: schemas.PostUserEvents):
    id:int = raw_data.id
    user_id:uuid.UUID = raw_data.user_id
    event_id:uuid.UUID = raw_data.event_id
    created_at:datetime.datetime = raw_data.created_at
    updated_at:datetime.datetime = raw_data.updated_at


    record_to_be_added = {'id': id, 'user_id': user_id, 'event_id': event_id, 'created_at': created_at, 'updated_at': updated_at}
    new_user_events = models.UserEvents(**record_to_be_added)
    db.add(new_user_events)
    db.commit()
    db.refresh(new_user_events)
    user_events_inserted_record = new_user_events.to_dict()

    res = {
        'user_events_inserted_record': user_events_inserted_record,
    }
    return res

async def put_user_events_id(db: Session, id: int, user_id: str, event_id: str, created_at: str, updated_at: str):

    user_events_edited_record = db.query(models.UserEvents).filter(models.UserEvents.id == id).first()
    for key, value in {'id': id, 'user_id': user_id, 'event_id': event_id, 'created_at': created_at, 'updated_at': updated_at}.items():
          setattr(user_events_edited_record, key, value)
    db.commit()
    db.refresh(user_events_edited_record)
    user_events_edited_record = user_events_edited_record.to_dict() 

    res = {
        'user_events_edited_record': user_events_edited_record,
    }
    return res

async def delete_user_events_id(db: Session, id: int):

    user_events_deleted = None
    record_to_delete = db.query(models.UserEvents).filter(models.UserEvents.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        user_events_deleted = record_to_delete.to_dict() 

    res = {
        'user_events_deleted': user_events_deleted,
    }
    return res

async def get_community_users_id(db: Session, id: int):

    community_users_one = db.query(models.CommunityUsers).filter(models.CommunityUsers.id == id).first() 
    community_users_one = community_users_one.to_dict() if community_users_one else community_users_one

    res = {
        'community_users_one': community_users_one,
    }
    return res

async def put_community_users_id(db: Session, id: int, community_id: str, user_id: str, created_at: str, updated_at: str, blocked: str):

    community_users_edited_record = db.query(models.CommunityUsers).filter(models.CommunityUsers.id == id).first()
    for key, value in {'id': id, 'blocked': blocked, 'user_id': user_id, 'created_at': created_at, 'updated_at': updated_at, 'community_id': community_id}.items():
          setattr(community_users_edited_record, key, value)
    db.commit()
    db.refresh(community_users_edited_record)
    community_users_edited_record = community_users_edited_record.to_dict() 

    res = {
        'community_users_edited_record': community_users_edited_record,
    }
    return res

async def delete_community_users_id(db: Session, id: int):

    community_users_deleted = None
    record_to_delete = db.query(models.CommunityUsers).filter(models.CommunityUsers.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        community_users_deleted = record_to_delete.to_dict() 

    res = {
        'community_users_deleted': community_users_deleted,
    }
    return res

async def get_post_comments(db: Session):

    post_comments_all = db.query(models.PostComments).all()
    post_comments_all = [new_data.to_dict() for new_data in post_comments_all] if post_comments_all else post_comments_all

    res = {
        'post_comments_all': post_comments_all,
    }
    return res

async def get_post_comments_id(db: Session, id: int):

    post_comments_one = db.query(models.PostComments).filter(models.PostComments.id == id).first() 
    post_comments_one = post_comments_one.to_dict() if post_comments_one else post_comments_one

    res = {
        'post_comments_one': post_comments_one,
    }
    return res

async def put_post_comments_id(db: Session, id: int, comment_id: str, post_id: str, user_id: str, comment: str, status_alias: str, created_at: str, updated_at: str):

    post_comments_edited_record = db.query(models.PostComments).filter(models.PostComments.id == id).first()
    for key, value in {'id': id, 'comment': comment, 'post_id': post_id, 'user_id': user_id, 'comment_id': comment_id, 'created_at': created_at, 'updated_at': updated_at, 'status_alias': status_alias}.items():
          setattr(post_comments_edited_record, key, value)
    db.commit()
    db.refresh(post_comments_edited_record)
    post_comments_edited_record = post_comments_edited_record.to_dict() 

    res = {
        'post_comments_edited_record': post_comments_edited_record,
    }
    return res

async def delete_post_comments_id(db: Session, id: int):

    post_comments_deleted = None
    record_to_delete = db.query(models.PostComments).filter(models.PostComments.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        post_comments_deleted = record_to_delete.to_dict() 

    res = {
        'post_comments_deleted': post_comments_deleted,
    }
    return res

async def post_post_comments(db: Session, raw_data: schemas.PostPostComments , request: Request):
    post_id:str = raw_data.post_id
    comment:str = raw_data.comment

    header_authorization:str = request.headers.get('header-authorization')



    try:
        decode_jwt2 = jwt.decode(
            header_authorization,
            'o3xsO1FLiEjpWhrCnAPqFgJ0cRu4W1DCaOU_RbfbZ6ZbH6GyN9K7IwFbTzwDqKc5',
            algorithms=['HS256']
        )
    except jwt.ExpiredSignatureError:
        decode_jwt2 = 'Token has expired.'
    except jwt.InvalidTokenError:
        decode_jwt2 = 'Invalid token.'

    res = {
        'decode_jwt': decode_jwt2,
        'authorization': header_authorization,
    }
    return res

async def post_attraction(db: Session, raw_data: schemas.PostAttraction , request: Request):
    id:int = raw_data.id
    name:str = raw_data.name
    url:str = raw_data.url
    event_id:uuid.UUID = raw_data.event_id

    header_authorization:str = request.headers.get('header-authorization')


    record_to_be_added = {'id': id, 'url': url, 'name': name, 'event_id': event_id}
    new_attraction = models.Attraction(**record_to_be_added)
    db.add(new_attraction)
    db.commit()
    db.refresh(new_attraction)
    attraction_inserted_record = new_attraction.to_dict()



    try:
        auth = jwt.decode(
            header_authorization,
            'o3xsO1FLiEjpWhrCnAPqFgJ0cRu4W1DCaOU_RbfbZ6ZbH6GyN9K7IwFbTzwDqKc5',
            algorithms=['HS256']
        )
    except jwt.ExpiredSignatureError:
        auth = 'Token has expired.'
    except jwt.InvalidTokenError:
        auth = 'Invalid token.'

    res = {
        'attraction_inserted_record': attraction_inserted_record,
        'auth': auth,
    }
    return res

