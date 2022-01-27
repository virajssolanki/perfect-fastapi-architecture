-- upgrade --
ALTER TABLE "user" RENAME COLUMN "refresh_token" TO "access_token";
-- downgrade --
ALTER TABLE "user" RENAME COLUMN "access_token" TO "refresh_token";
