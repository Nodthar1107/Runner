import PlayableCharacter
import BushContainer
import Rectangle 

class RectCollisionMediator:
    def isRectCollided(self, mainRect, rect):
        if (mainRect["top_left"]["x"] <= rect["top_left"]["x"] and
            mainRect["top_left"]["y"] <= rect["top_left"]["y"] and
            mainRect["bottom_right"]["x"] >= rect["top_left"]["x"] and
            mainRect["bottom_right"]["y"] >= rect["top_left"]["y"]):
            return True

        if (mainRect["top_left"]["x"] <= rect["top_right"]["x"] and
            mainRect["top_left"]["y"] <= rect["top_right"]["y"] and
            mainRect["bottom_right"]["x"] >= rect["top_right"]["x"] and
            mainRect["bottom_right"]["y"] >= rect["top_right"]["y"]):
            return True

        if (mainRect["top_left"]["x"] <= rect["bottom_left"]["x"] and
            mainRect["top_left"]["y"] <= rect["bottom_left"]["y"] and
            mainRect["bottom_right"]["x"] >= rect["bottom_left"]["x"] and
            mainRect["bottom_right"]["y"] >= rect["bottom_left"]["y"]):
            return True

        if (mainRect["top_left"]["x"] <= rect["bottom_right"]["x"] and
            mainRect["top_left"]["y"] <= rect["bottom_right"]["y"] and
            mainRect["bottom_right"]["x"] >= rect["bottom_right"]["x"] and
            mainRect["bottom_right"]["y"] >= rect["bottom_right"]["y"]):
            return True
        
        return False

class CharacterAndBushesCollisionMediator(RectCollisionMediator):

    def isCollided(self, character, bushes):
        character_rect = character.get_collision_box()

        for bush in bushes:
            if super().isRectCollided(character_rect, bush.get_collision_box()):
                return True

        return False