-- upgrade --
ALTER TABLE "user" DROP COLUMN "access_token";
-- downgrade --
ALTER TABLE "user" ADD "access_token" UUID;
