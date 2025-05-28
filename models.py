from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import class_mapper
import uuid
from datetime import datetime
from decimal import Decimal

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Time, Float, Text, ForeignKey, JSON, Numeric, Date, \
    TIMESTAMP, UUID
from sqlalchemy.ext.declarative import declarative_base


@as_declarative()
class Base:
    id: int
    __name__: str

    # Auto-generate table name if not provided
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    # Generic to_dict() method
    def to_dict(self):
        """
        Converts the SQLAlchemy model instance to a dictionary, ensuring UUID fields are converted to strings.
        """
        result = {}
        for column in class_mapper(self.__class__).columns:
            value = getattr(self, column.key)
                # Handle UUID fields
            if isinstance(value, uuid.UUID):
                value = str(value)
            # Handle datetime fields
            elif isinstance(value, datetime):
                value = value.isoformat()  # Convert to ISO 8601 string
            # Handle Decimal fields
            elif isinstance(value, Decimal):
                value = float(value)

            result[column.key] = value
        return result




class Image(Base):
    __tablename__ = 'image'
    id = Column(Integer, primary_key=True)
    ratio = Column(String, primary_key=False)
    width = Column(Integer, primary_key=False)
    height = Column(Integer, primary_key=False)
    fallback = Column(Boolean, primary_key=False)
    event_id = Column(UUID, primary_key=False)


class Event(Base):
    __tablename__ = 'event'
    id = Column(Integer, primary_key=True)
    name = Column(String, primary_key=False)
    type = Column(String, primary_key=False)
    url = Column(String, primary_key=False)
    locale = Column(String, primary_key=False)
    segment = Column(String, primary_key=False)
    genre = Column(String, primary_key=False)
    sub_genre = Column(String, primary_key=False)
    event_type = Column(String, primary_key=False)
    sub_type = Column(String, primary_key=False)
    min_price = Column(String, primary_key=False)
    max_price = Column(String, primary_key=False)
    currency_type = Column(String, primary_key=False)
    seatmap_url = Column(String, primary_key=False)
    safe_tix = Column(Boolean, primary_key=False)
    min_age = Column(Integer, primary_key=False)
    ticket_limit = Column(String, primary_key=False)
    accessibility_limit = Column(String, primary_key=False)
    all_inclusive_pricing = Column(Boolean, primary_key=False)
    created_at = Column(Time, primary_key=False)
    updated_at = Column(Time, primary_key=False)
    date_id = Column(Integer, primary_key=False)
    venue_id = Column(Integer, primary_key=False)
    event_id = Column(UUID, primary_key=False)
    is_trending = Column(Boolean, primary_key=False)
    is_active = Column(Boolean, primary_key=False)


class Date(Base):
    __tablename__ = 'date'
    id = Column(Integer, primary_key=True)
    timezone = Column(String, primary_key=False)
    status = Column(String, primary_key=False)
    span_multiple_days = Column(Boolean, primary_key=False)
    local_date = Column(String, primary_key=False)
    local_time = Column(String, primary_key=False)
    datetime = Column(Time, primary_key=False)
    date_tbd = Column(Boolean, primary_key=False)
    date_tba = Column(Boolean, primary_key=False)
    time_tba = Column(Boolean, primary_key=False)
    no_specific_time = Column(Boolean, primary_key=False)


class Venue(Base):
    __tablename__ = 'venue'
    id = Column(Integer, primary_key=True)
    name = Column(String, primary_key=False)
    type = Column(String, primary_key=False)
    url = Column(String, primary_key=False)
    locale = Column(String, primary_key=False)
    postal_code = Column(String, primary_key=False)
    timezone = Column(String, primary_key=False)
    city = Column(String, primary_key=False)
    state = Column(String, primary_key=False)
    country = Column(String, primary_key=False)
    country_code = Column(String, primary_key=False)
    address_line1 = Column(String, primary_key=False)
    longitude = Column(Float, primary_key=False)
    latitude = Column(Float, primary_key=False)
    phone_number_detail = Column(String, primary_key=False)
    open_hours_detail = Column(String, primary_key=False)
    accepted_payment_detail = Column(String, primary_key=False)
    will_call_detail = Column(String, primary_key=False)
    created_at = Column(Time, primary_key=False)
    updated_at = Column(Time, primary_key=False)


class PostsLike(Base):
    __tablename__ = 'posts_like'
    id = Column(Integer, primary_key=True)
    user_id = Column(UUID, primary_key=False)
    post_id = Column(UUID, primary_key=False)
    reaction_alias = Column(String, primary_key=False)


class Posts(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    post_id = Column(UUID, primary_key=False)
    community_id = Column(UUID, primary_key=False)
    user_id = Column(UUID, primary_key=False)
    caption = Column(String, primary_key=False)
    image = Column(String, primary_key=False)
    status_alias = Column(String, primary_key=False)
    created_at = Column(Time, primary_key=False)
    updated_at = Column(Time, primary_key=False)
    post_type = Column(String, primary_key=False)
    ref_event_id = Column(String, primary_key=False)


class Communities(Base):
    __tablename__ = 'communities'
    id = Column(Integer, primary_key=True)
    community_id = Column(UUID, primary_key=False)
    name = Column(String, primary_key=False)
    description = Column(String, primary_key=False)
    image = Column(String, primary_key=False)
    category = Column(String, primary_key=False)
    type = Column(String, primary_key=False)
    admin_id = Column(UUID, primary_key=False)
    status_alias = Column(String, primary_key=False)
    created_at = Column(Time, primary_key=False)
    updated_at = Column(Time, primary_key=False)
    is_active = Column(Boolean, primary_key=False)


class User(Base):
    __tablename__ = 'user'
    user_id = Column(UUID, primary_key=True)
    name = Column(String, primary_key=False)
    email = Column(String, primary_key=False)
    phone = Column(String, primary_key=False)
    country_code = Column(String, primary_key=False)
    google_id = Column(String, primary_key=False)
    apple_id = Column(String, primary_key=False)
    created_at = Column(Time, primary_key=False)
    updated_at = Column(Time, primary_key=False)
    gender = Column(String, primary_key=False)
    last_login = Column(Time, primary_key=False)
    user_avatar = Column(String, primary_key=False)
    is_blocked = Column(Boolean, primary_key=False)
    password = Column(String, primary_key=False)
    password_reset_token = Column(String, primary_key=False)
    password_reset_expires = Column(Time, primary_key=False)
    email_verified = Column(Boolean, primary_key=False)
    last_password_change = Column(Time, primary_key=False)
    id = Column(Integer, primary_key=False)
    streak = Column(Integer, primary_key=False)


class Attraction(Base):
    __tablename__ = 'attraction'
    id = Column(Integer, primary_key=True)
    name = Column(String, primary_key=False)
    url = Column(String, primary_key=False)
    event_id = Column(UUID, primary_key=False)


class CrmUsers(Base):
    __tablename__ = 'crm_users'
    id = Column(Integer, primary_key=True)
    crm_id = Column(UUID, primary_key=False)
    name = Column(String, primary_key=False)
    email = Column(String, primary_key=False)
    password = Column(String, primary_key=False)
    recovery_number = Column(String, primary_key=False)
    designation = Column(String, primary_key=False)
    department = Column(String, primary_key=False)
    role = Column(String, primary_key=False)
    created_at = Column(Time, primary_key=False)
    updated_at = Column(Time, primary_key=False)
    is_blocked = Column(Boolean, primary_key=False)


class Reward(Base):
    __tablename__ = 'reward'
    id = Column(Integer, primary_key=True)
    reward_id = Column(UUID, primary_key=False)
    name = Column(String, primary_key=False)
    alias = Column(String, primary_key=False)
    reward_on = Column(String, primary_key=False)
    value = Column(String, primary_key=False)
    frequency = Column(Integer, primary_key=False)
    img_url = Column(String, primary_key=False)
    creted_at = Column(Time, primary_key=False)
    updated_at = Column(Time, primary_key=False)
    reward_type = Column(String, primary_key=False)
    earn_bonus = Column(String, primary_key=False)
    sub_description = Column(String, primary_key=False)
    is_active = Column(Boolean, primary_key=False)


class QuestionMaster(Base):
    __tablename__ = 'question_master'
    type = Column(String, primary_key=False)
    question = Column(String, primary_key=False)
    status = Column(String, primary_key=False)
    created_at = Column(Time, primary_key=False)
    updated_at = Column(Time, primary_key=False)
    created_by = Column(String, primary_key=False)
    updated_by = Column(String, primary_key=False)
    is_active = Column(Boolean, primary_key=False)
    min_range = Column(Integer, primary_key=False)
    max_range = Column(Integer, primary_key=False)
    id = Column(Integer, primary_key=True)


class UserSessions(Base):
    __tablename__ = 'user_sessions'
    session_id = Column(String, primary_key=True)
    user_id = Column(UUID, primary_key=False)
    device_type = Column(String, primary_key=False)
    device_id = Column(String, primary_key=False)
    app_version = Column(String, primary_key=False)
    os_version = Column(String, primary_key=False)
    access_token = Column(String, primary_key=False)
    refresh_token = Column(String, primary_key=False)
    ip_address = Column(String, primary_key=False)
    user_agent = Column(String, primary_key=False)
    location = Column(String, primary_key=False)
    login_time = Column(Time, primary_key=False)
    last_activity = Column(Time, primary_key=False)
    expiration_time = Column(Time, primary_key=False)
    status = Column(String, primary_key=False)
    created_at = Column(Time, primary_key=False)
    updated_at = Column(Time, primary_key=False)


class UserBucketlist(Base):
    __tablename__ = 'user_bucketlist'
    user_id = Column(UUID, primary_key=False)
    event_id = Column(UUID, primary_key=False)
    has_booked = Column(Boolean, primary_key=False)
    booked_time = Column(Time, primary_key=False)
    created_at = Column(Time, primary_key=False)
    id = Column(Integer, primary_key=True)


class UserSurvey(Base):
    __tablename__ = 'user_survey'
    created_at = Column(Time, primary_key=False)
    updated_at = Column(Time, primary_key=False)
    user_id = Column(UUID, primary_key=False)
    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, primary_key=False)
    answer_id = Column(Integer, primary_key=False)


class UserReward(Base):
    __tablename__ = 'user_reward'
    id = Column(Integer, primary_key=True)
    user_id = Column(UUID, primary_key=False)
    reward_id = Column(UUID, primary_key=False)
    reward_value = Column(Integer, primary_key=False)
    creted_at = Column(Time, primary_key=False)
    updated_at = Column(Time, primary_key=False)
    is_visible = Column(Boolean, primary_key=False)


class UserEvents(Base):
    __tablename__ = 'user_events'
    id = Column(Integer, primary_key=True)
    user_id = Column(UUID, primary_key=False)
    event_id = Column(UUID, primary_key=False)
    created_at = Column(Time, primary_key=False)
    updated_at = Column(Time, primary_key=False)


class CommunityUsers(Base):
    __tablename__ = 'community_users'
    id = Column(Integer, primary_key=True)
    community_id = Column(UUID, primary_key=False)
    user_id = Column(UUID, primary_key=False)
    created_at = Column(Time, primary_key=False)
    updated_at = Column(Time, primary_key=False)
    blocked = Column(Boolean, primary_key=False)


class PostComments(Base):
    __tablename__ = 'post_comments'
    id = Column(Integer, primary_key=True)
    comment_id = Column(UUID, primary_key=False)
    post_id = Column(UUID, primary_key=False)
    user_id = Column(UUID, primary_key=False)
    comment = Column(String, primary_key=False)
    status_alias = Column(String, primary_key=False)
    created_at = Column(Time, primary_key=False)
    updated_at = Column(Time, primary_key=False)


