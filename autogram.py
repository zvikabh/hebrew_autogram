import itertools
import numpy as np

STORY = '''
סיפור
היה היתה פעם משפחה-חה גרעינית בשם משפחת בן-חיים, שאהבה מאוד סיפורים,
ובה חמישה אנשים שקראו להם צ'ומפי, נוני, יותיות, נימנים וחבובה ישן.
אני רוצה לשמוע סיפור שיש בו * צ'ים, אמרה צ'ומפי.
לא, אמרה נוני, ספרו לנו סיפור שיש בו * נ'ים.
אבל אני רוצה סיפור שיש בו * י'ים, אמר יותיות.
ונימנים, שקראו לה גם אמא, אמרה: אני דווקא רוצה סיפור עם * א'ים ועם * מ'ים.
אה ככה? אמר חבובה ישן. אם כך אספר לכם סיפור שיש בו * ח'ים.
וזה הסיפור.
יפטו.
'''

DIGITS = [
  'אחד',
  'שנים',
  'שלושה',
  'ארבעה',
  'חמישה',
  'שישה',
  'שבעה',
  'שמונה',
  'תשעה']
NUMS = ['אפס'] + DIGITS + ['עשרה']
NUMS.extend(f'{digit} עשר' for digit in DIGITS)

TENS = ['עשרים', 'שלושים', 'ארבעים', 'חמישים', 'שישים', 'שבעים', 'שמונים', 'תשעים']

for ten in TENS:
  NUMS.append(ten)
  NUMS.extend(f'{ten} ו{digit}' for digit in DIGITS)


LETTER_POSITIONS = {}
for pos, letter in enumerate('אבגדהוזחטיכלמנסעפצקרשת'):
  LETTER_POSITIONS[letter] = pos
LETTER_POSITIONS['ך'] = LETTER_POSITIONS['כ']
LETTER_POSITIONS['ם'] = LETTER_POSITIONS['מ']
LETTER_POSITIONS['ן'] = LETTER_POSITIONS['נ']
LETTER_POSITIONS['ף'] = LETTER_POSITIONS['פ']
LETTER_POSITIONS['ץ'] = LETTER_POSITIONS['צ']


def count(s: str) -> np.ndarray:
  c = np.zeros(22, dtype=np.int32)
  for ch in s:
    if ch in LETTER_POSITIONS:
      c[LETTER_POSITIONS[ch]] += 1
  return c


def main():
  story_count = count(STORY)
  target_letters = ['צ', 'נ', 'י', 'א', 'מ', 'ח']
  min_vals = [story_count[LETTER_POSITIONS[letter]] for letter in target_letters]
  ranges = [range(min_val, min_val + 10) for min_val in min_vals]
  for proposal in itertools.product(*ranges):
    addition_to_story = ' '.join(NUMS[p] for p in proposal)
    total_count = story_count + count(addition_to_story)
    valid_solution = True
    for letter, proposed in zip(target_letters, proposal):
      if total_count[LETTER_POSITIONS[letter]] != proposed:
        valid_solution = False
        break
    if valid_solution:
      print(proposal)


if __name__ == '__main__':
  main()
