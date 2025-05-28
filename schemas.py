from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List, Tuple

class Image(BaseModel):
    id: int
    ratio: str
    width: int
    height: int
    fallback: bool
    event_id: uuid.UUID


class ReadImage(BaseModel):
    id: int
    ratio: str
    width: int
    height: int
    fallback: bool
    event_id: uuid.UUID
    class Config:
        from_attributes = True


class Event(BaseModel):
    id: int
    name: str
    type: str
    url: str
    locale: str
    segment: str
    genre: str
    sub_genre: str
    event_type: str
    sub_type: str
    min_price: str
    max_price: str
    currency_type: str
    seatmap_url: str
    safe_tix: bool
    min_age: int
    ticket_limit: str
    accessibility_limit: str
    all_inclusive_pricing: bool
    created_at: datetime.time
    updated_at: datetime.time
    date_id: int
    venue_id: int
    event_id: uuid.UUID
    is_trending: bool
    is_active: bool


class ReadEvent(BaseModel):
    id: int
    name: str
    type: str
    url: str
    locale: str
    segment: str
    genre: str
    sub_genre: str
    event_type: str
    sub_type: str
    min_price: str
    max_price: str
    currency_type: str
    seatmap_url: str
    safe_tix: bool
    min_age: int
    ticket_limit: str
    accessibility_limit: str
    all_inclusive_pricing: bool
    created_at: datetime.time
    updated_at: datetime.time
    date_id: int
    venue_id: int
    event_id: uuid.UUID
    is_trending: bool
    is_active: bool
    class Config:
        from_attributes = True


class Date(BaseModel):
    id: int
    timezone: str
    status: str
    span_multiple_days: bool
    local_date: str
    local_time: str
    datetime: datetime.time
    date_tbd: bool
    date_tba: bool
    time_tba: bool
    no_specific_time: bool


class ReadDate(BaseModel):
    id: int
    timezone: str
    status: str
    span_multiple_days: bool
    local_date: str
    local_time: str
    datetime: datetime.time
    date_tbd: bool
    date_tba: bool
    time_tba: bool
    no_specific_time: bool
    class Config:
        from_attributes = True


class Venue(BaseModel):
    id: int
    name: str
    type: str
    url: str
    locale: str
    postal_code: str
    timezone: str
    city: str
    state: str
    country: str
    country_code: str
    address_line1: str
    longitude: float
    latitude: float
    phone_number_detail: str
    open_hours_detail: str
    accepted_payment_detail: str
    will_call_detail: str
    created_at: datetime.time
    updated_at: datetime.time


class ReadVenue(BaseModel):
    id: int
    name: str
    type: str
    url: str
    locale: str
    postal_code: str
    timezone: str
    city: str
    state: str
    country: str
    country_code: str
    address_line1: str
    longitude: float
    latitude: float
    phone_number_detail: str
    open_hours_detail: str
    accepted_payment_detail: str
    will_call_detail: str
    created_at: datetime.time
    updated_at: datetime.time
    class Config:
        from_attributes = True


class PostsLike(BaseModel):
    id: int
    user_id: uuid.UUID
    post_id: uuid.UUID
    reaction_alias: str


class ReadPostsLike(BaseModel):
    id: int
    user_id: uuid.UUID
    post_id: uuid.UUID
    reaction_alias: str
    class Config:
        from_attributes = True


class Posts(BaseModel):
    id: int
    post_id: uuid.UUID
    community_id: uuid.UUID
    user_id: uuid.UUID
    caption: str
    image: str
    status_alias: str
    created_at: datetime.time
    updated_at: datetime.time
    post_type: str
    ref_event_id: str


class ReadPosts(BaseModel):
    id: int
    post_id: uuid.UUID
    community_id: uuid.UUID
    user_id: uuid.UUID
    caption: str
    image: str
    status_alias: str
    created_at: datetime.time
    updated_at: datetime.time
    post_type: str
    ref_event_id: str
    class Config:
        from_attributes = True


class Communities(BaseModel):
    id: int
    community_id: uuid.UUID
    name: str
    description: str
    image: str
    category: str
    type: str
    admin_id: uuid.UUID
    status_alias: str
    created_at: datetime.time
    updated_at: datetime.time
    is_active: bool


class ReadCommunities(BaseModel):
    id: int
    community_id: uuid.UUID
    name: str
    description: str
    image: str
    category: str
    type: str
    admin_id: uuid.UUID
    status_alias: str
    created_at: datetime.time
    updated_at: datetime.time
    is_active: bool
    class Config:
        from_attributes = True


class User(BaseModel):
    user_id: uuid.UUID
    name: str
    email: str
    phone: str
    country_code: str
    google_id: str
    apple_id: str
    created_at: datetime.time
    updated_at: datetime.time
    gender: str
    last_login: datetime.time
    user_avatar: str
    is_blocked: bool
    password: str
    password_reset_token: str
    password_reset_expires: datetime.time
    email_verified: bool
    last_password_change: datetime.time
    id: int
    streak: int


class ReadUser(BaseModel):
    user_id: uuid.UUID
    name: str
    email: str
    phone: str
    country_code: str
    google_id: str
    apple_id: str
    created_at: datetime.time
    updated_at: datetime.time
    gender: str
    last_login: datetime.time
    user_avatar: str
    is_blocked: bool
    password: str
    password_reset_token: str
    password_reset_expires: datetime.time
    email_verified: bool
    last_password_change: datetime.time
    id: int
    streak: int
    class Config:
        from_attributes = True


class Attraction(BaseModel):
    id: int
    name: str
    url: str
    event_id: uuid.UUID


class ReadAttraction(BaseModel):
    id: int
    name: str
    url: str
    event_id: uuid.UUID
    class Config:
        from_attributes = True


class CrmUsers(BaseModel):
    id: int
    crm_id: uuid.UUID
    name: str
    email: str
    password: str
    recovery_number: str
    designation: str
    department: str
    role: str
    created_at: datetime.time
    updated_at: datetime.time
    is_blocked: bool


class ReadCrmUsers(BaseModel):
    id: int
    crm_id: uuid.UUID
    name: str
    email: str
    password: str
    recovery_number: str
    designation: str
    department: str
    role: str
    created_at: datetime.time
    updated_at: datetime.time
    is_blocked: bool
    class Config:
        from_attributes = True


class Reward(BaseModel):
    id: int
    reward_id: uuid.UUID
    name: str
    alias: str
    reward_on: str
    value: str
    frequency: int
    img_url: str
    creted_at: datetime.time
    updated_at: datetime.time
    reward_type: str
    earn_bonus: str
    sub_description: str
    is_active: bool


class ReadReward(BaseModel):
    id: int
    reward_id: uuid.UUID
    name: str
    alias: str
    reward_on: str
    value: str
    frequency: int
    img_url: str
    creted_at: datetime.time
    updated_at: datetime.time
    reward_type: str
    earn_bonus: str
    sub_description: str
    is_active: bool
    class Config:
        from_attributes = True


class QuestionMaster(BaseModel):
    type: str
    question: str
    status: str
    created_at: datetime.time
    updated_at: datetime.time
    created_by: str
    updated_by: str
    is_active: bool
    min_range: int
    max_range: int
    id: int


class ReadQuestionMaster(BaseModel):
    type: str
    question: str
    status: str
    created_at: datetime.time
    updated_at: datetime.time
    created_by: str
    updated_by: str
    is_active: bool
    min_range: int
    max_range: int
    id: int
    class Config:
        from_attributes = True


class UserSessions(BaseModel):
    session_id: str
    user_id: uuid.UUID
    device_type: str
    device_id: str
    app_version: str
    os_version: str
    access_token: str
    refresh_token: str
    ip_address: str
    user_agent: str
    location: str
    login_time: datetime.time
    last_activity: datetime.time
    expiration_time: datetime.time
    status: str
    created_at: datetime.time
    updated_at: datetime.time


class ReadUserSessions(BaseModel):
    session_id: str
    user_id: uuid.UUID
    device_type: str
    device_id: str
    app_version: str
    os_version: str
    access_token: str
    refresh_token: str
    ip_address: str
    user_agent: str
    location: str
    login_time: datetime.time
    last_activity: datetime.time
    expiration_time: datetime.time
    status: str
    created_at: datetime.time
    updated_at: datetime.time
    class Config:
        from_attributes = True


class UserBucketlist(BaseModel):
    user_id: uuid.UUID
    event_id: uuid.UUID
    has_booked: bool
    booked_time: datetime.time
    created_at: datetime.time
    id: int


class ReadUserBucketlist(BaseModel):
    user_id: uuid.UUID
    event_id: uuid.UUID
    has_booked: bool
    booked_time: datetime.time
    created_at: datetime.time
    id: int
    class Config:
        from_attributes = True


class UserSurvey(BaseModel):
    created_at: datetime.time
    updated_at: datetime.time
    user_id: uuid.UUID
    id: int
    question_id: int
    answer_id: int


class ReadUserSurvey(BaseModel):
    created_at: datetime.time
    updated_at: datetime.time
    user_id: uuid.UUID
    id: int
    question_id: int
    answer_id: int
    class Config:
        from_attributes = True


class UserReward(BaseModel):
    id: int
    user_id: uuid.UUID
    reward_id: uuid.UUID
    reward_value: int
    creted_at: datetime.time
    updated_at: datetime.time
    is_visible: bool


class ReadUserReward(BaseModel):
    id: int
    user_id: uuid.UUID
    reward_id: uuid.UUID
    reward_value: int
    creted_at: datetime.time
    updated_at: datetime.time
    is_visible: bool
    class Config:
        from_attributes = True


class UserEvents(BaseModel):
    id: int
    user_id: uuid.UUID
    event_id: uuid.UUID
    created_at: datetime.time
    updated_at: datetime.time


class ReadUserEvents(BaseModel):
    id: int
    user_id: uuid.UUID
    event_id: uuid.UUID
    created_at: datetime.time
    updated_at: datetime.time
    class Config:
        from_attributes = True


class CommunityUsers(BaseModel):
    id: int
    community_id: uuid.UUID
    user_id: uuid.UUID
    created_at: datetime.time
    updated_at: datetime.time
    blocked: bool


class ReadCommunityUsers(BaseModel):
    id: int
    community_id: uuid.UUID
    user_id: uuid.UUID
    created_at: datetime.time
    updated_at: datetime.time
    blocked: bool
    class Config:
        from_attributes = True


class PostComments(BaseModel):
    id: int
    comment_id: uuid.UUID
    post_id: uuid.UUID
    user_id: uuid.UUID
    comment: str
    status_alias: str
    created_at: datetime.time
    updated_at: datetime.time


class ReadPostComments(BaseModel):
    id: int
    comment_id: uuid.UUID
    post_id: uuid.UUID
    user_id: uuid.UUID
    comment: str
    status_alias: str
    created_at: datetime.time
    updated_at: datetime.time
    class Config:
        from_attributes = True




class PostCommunities(BaseModel):
    id: int
    community_id: str
    name: str
    description: str
    image: str
    category: str
    type: str
    admin_id: str
    status_alias: str
    created_at: str
    updated_at: str
    is_active: bool

    class Config:
        from_attributes = True



class PostCommunityUsers(BaseModel):
    id: int
    community_id: str
    user_id: str
    created_at: str
    updated_at: str
    blocked: bool

    class Config:
        from_attributes = True



class PostUser(BaseModel):
    name: str
    email: str
    phone: str
    country_code: str
    gender: str
    user_avatar: str
    password: str
    streak: int
    is_blocked: bool

    class Config:
        from_attributes = True



class PostLogin(BaseModel):
    email: str
    password: str

    class Config:
        from_attributes = True



class PostImage(BaseModel):
    id: int
    ratio: str
    url: str
    width: int
    height: int
    fallback: bool
    event_id: Any

    class Config:
        from_attributes = True



class PostEvent(BaseModel):
    id: int
    name: str
    type: str
    url: str
    locale: str
    segment: str
    genre: str
    sub_genre: str
    event_type: str
    sub_type: str
    min_price: str
    max_price: str
    currency_type: str
    seatmap_url: str
    safe_tix: bool
    min_age: int
    ticket_limit: str
    accessibility_limit: str
    all_inclusive_pricing: bool
    created_at: Any
    updated_at: Any
    date_id: int
    venue_id: int
    event_id: Any
    is_trending: bool
    is_active: bool

    class Config:
        from_attributes = True



class PostDate(BaseModel):
    id: int
    timezone: str
    status: str
    span_multiple_days: bool
    local_date: str
    local_time: str
    datetime: Any
    date_tbd: bool
    date_tba: bool
    time_tba: bool
    no_specific_time: bool

    class Config:
        from_attributes = True



class PostVenue(BaseModel):
    id: int
    name: str
    type: str
    url: str
    locale: str
    postal_code: str
    timezone: str
    city: str
    state: str
    country: str
    country_code: str
    address_line1: str
    longitude: Any
    latitude: Any
    phone_number_detail: str
    open_hours_detail: str
    accepted_payment_detail: str
    will_call_detail: str
    created_at: Any
    updated_at: Any

    class Config:
        from_attributes = True



class PostPostsLike(BaseModel):
    id: int
    user_id: Any
    post_id: Any
    reaction_alias: str

    class Config:
        from_attributes = True



class PostPosts(BaseModel):
    id: int
    post_id: Any
    community_id: Any
    user_id: Any
    caption: str
    image: str
    status_alias: str
    created_at: Any
    updated_at: Any
    post_type: str
    ref_event_id: str

    class Config:
        from_attributes = True



class PostCrmUsers(BaseModel):
    id: int
    crm_id: Any
    name: str
    email: str
    password: str
    recovery_number: str
    designation: str
    department: str
    role: str
    created_at: Any
    updated_at: Any
    is_blocked: bool

    class Config:
        from_attributes = True



class PostReward(BaseModel):
    id: int
    reward_id: Any
    name: str
    alias: str
    reward_on: str
    value: str
    frequency: int
    img_url: str
    creted_at: Any
    updated_at: Any
    reward_type: str
    earn_bonus: str
    sub_description: str
    is_active: bool

    class Config:
        from_attributes = True



class PostQuestionMaster(BaseModel):
    type: str
    question: str
    status: str
    created_at: Any
    updated_at: Any
    created_by: str
    updated_by: str
    is_active: bool
    min_range: int
    max_range: int
    id: int

    class Config:
        from_attributes = True



class PostUserSessions(BaseModel):
    session_id: str
    user_id: Any
    device_type: str
    device_id: str
    app_version: str
    os_version: str
    access_token: str
    refresh_token: str
    ip_address: str
    user_agent: str
    location: str
    login_time: Any
    last_activity: Any
    expiration_time: Any
    status: str
    created_at: Any
    updated_at: Any

    class Config:
        from_attributes = True



class PostUserBucketlist(BaseModel):
    user_id: Any
    event_id: Any
    has_booked: bool
    booked_time: Any
    created_at: Any
    id: int

    class Config:
        from_attributes = True



class PostUserSurvey(BaseModel):
    created_at: Any
    updated_at: Any
    user_id: Any
    id: int
    question_id: int
    answer_id: int

    class Config:
        from_attributes = True



class PostUserReward(BaseModel):
    id: int
    user_id: Any
    reward_id: Any
    reward_value: int
    creted_at: Any
    updated_at: Any
    is_visible: bool

    class Config:
        from_attributes = True



class PostUserEvents(BaseModel):
    id: int
    user_id: Any
    event_id: Any
    created_at: Any
    updated_at: Any

    class Config:
        from_attributes = True



class PostPostComments(BaseModel):
    post_id: str
    comment: str

    class Config:
        from_attributes = True



class PostAttraction(BaseModel):
    id: int
    name: str
    url: str
    event_id: Any

    class Config:
        from_attributes = True

