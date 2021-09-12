-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/a4u9hc
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

-- Modify this code to update the DB schema diagram.
-- To reset the sample schema, replace everything with
-- two dots ('..' - without quotes).

DROP TABLE "sqf_merged_data"
CREATE TABLE "sqf_merged_data" (
    "year" int   NOT NULL,
    "month" varchar   NOT NULL,
    "day" varchar   NOT NULL,
    "stop_was_initiated" varchar   NOT NULL,
    "issuing_officer_rank" varchar   NOT NULL,
    "observed_duration_minutes" float   NOT NULL,
    "suspected_crime_description" varchar   NOT NULL,
    "stop_duration_minutes" float   NOT NULL,
    "officer_explained_stop_flag" varchar   NOT NULL,
    "suspect_arrested_flag" varchar   NOT NULL,
    "summons_issued_flag" varchar   NOT NULL,
    "officer_in_uniform_flag" varchar   NOT NULL,
    "frisked_flag" varchar   NOT NULL,
    "searched_flag" varchar   NOT NULL,
    "weapon_found_flag" varchar   NOT NULL,
    "suspect_reported_age" varchar   NOT NULL,
    "suspect_sex" varchar   NOT NULL,
    "suspect_race_description" varchar   NOT NULL,
    "suspect_height" varchar   NOT NULL,
    "suspect_weight" varchar   NOT NULL,
    "suspect_body_build_type" varchar   NOT NULL,
    "suspect_eye_color" varchar   NOT NULL,
    "suspect_hair_color" varchar   NOT NULL,
    "stop_location_x" varchar   NOT NULL,
    "stop_location_y" varchar   NOT NULL,
    "stop_location_boro_name" varchar   NOT NULL,
    "seconds" float   NOT NULL
);

CREATE TABLE "sqf_2020_data" (
    "year" int   NOT NULL,
    "month" varchar   NOT NULL,
    "day" varchar   NOT NULL,
    "stop_was_initiated" varchar   NOT NULL,
    "issuing_officer_rank" varchar   NOT NULL,
    "observed_duration_minutes" int   NOT NULL,
    "suspected_crime_description" varchar   NOT NULL,
    "stop_duration_minutes" int   NOT NULL,
    "officer_explained_stop_flag" varchar   NOT NULL,
    "suspect_arrested_flag" varchar   NOT NULL,
    "summons_issued_flag" varchar   NOT NULL,
    "officer_in_uniform_flag" varchar   NOT NULL,
    "frisked_flag" varchar   NOT NULL,
    "searched_flag" varchar   NOT NULL,
    "weapon_found_flag" varchar   NOT NULL,
    "suspect_reported_age" varchar   NOT NULL,
    "suspect_sex" varchar   NOT NULL,
    "suspect_race_description" varchar   NOT NULL,
    "suspect_height" varchar   NOT NULL,
    "suspect_weight" varchar   NOT NULL,
    "suspect_body_build_type" varchar   NOT NULL,
    "suspect_eye_color" varchar   NOT NULL,
    "suspect_hair_color" varchar   NOT NULL,
    "stop_location_x" varchar   NOT NULL,
    "stop_location_y" varchar   NOT NULL,
    "stop_location_boro_name" varchar   NOT NULL,
    "seconds" float   NOT NULL
);

SELECT * FROM "sqf_2020_data"

SELECT * FROM "sqf_merged_data"
WHERE year = 2017;
