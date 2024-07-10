LOAD DATA
INFILE '..\data\gyeonggi_card.csv'
INTO TABLE card_sample
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
(
  a_ymd "TO_DATE(:a_ymd, 'YYYYMMDD')",
  cty_rgn_no,
  admi_cty_no,
  card_tpbuz_cd,
  card_tpbuz_nm_1,
  card_tpbuz_nm_2,
  hour,
  sex,
  age,
  day,
  amt,
  cnt
)

