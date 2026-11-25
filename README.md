# The World in One Day — 25 November 2026

[![news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/m1651/makefun-news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/m1651/makefun-news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

A one-image summary of the world's news of **Wednesday 25 November 2026**,
drawn as a newspaper front page. The program ships the image in this
repository and copies it to the output directory as `entry.png`.

## What the image shows

The masthead names the day in large type — **25 NOVEMBER 2026** — above
eight stories from across regions and fields, plus a footer strip:

- **Lead story, war in Ukraine:** Zelenskiy confirms Ukraine's drones hit
  a Russian cargo ship in the Gulf of Finland, days after sinking the
  corvette Merkury in Libya's Benghazi port. Norway urges caution as the
  war spreads.
- **Middle East:** a Houthi strike hits Riyadh's tallest tower, the PIF
  tower, for the second time in five days. Eleven people are wounded;
  Riyadh condemns a "terrorist attack".
- **Tech and markets:** Nvidia shares fall about 5% a day after jumping
  31% on Jensen Huang's return as chief executive. Huang tells staff he
  made "terrible mistakes" and is "in therapy".
- **China:** Beijing opens a shock corruption investigation into Politburo
  member and Shanghai party chief Chen Jining.
- **USA, courts:** a US jury convicts Huawei of conspiracy to steal trade
  secrets and bank fraud.
- **USA:** Trump pardons the Thanksgiving turkeys Freedom and Feathers,
  and awards Rudy Giuliani the Medal of Freedom.
- **Sport:** the Court of Arbitration for Sport hands the Africa Cup title
  back to Senegal, overturning the ruling that gave it to Morocco.
- **Space:** Pakistani astronaut Muhammad Zeeshan Ali joins Shenzhou-24 —
  the first foreigner aboard China's space station.
- **Also:** the CIA and the ODNI are hit by a cyber breach; Sarkozy's
  corruption case goes to trial; a Hamas security chief is killed in a
  Gaza strike; gunmen take 25 hostages in Colombia; Gukesh holds Sindarov
  in the world chess title match.

## How the image was made

Every pixel is original work drawn in this session with Python (Pillow)
and the DejaVu fonts: the masthead, the globe, the market figures and
every card and label are code-drawn shapes and text. No photograph,
artwork or existing image was downloaded, copied or reused. The finished
image is stored in this repository as `entry.png`.

## Running it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` uses only the Python standard library, needs no network, and
copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`. It checks the PNG
signature before copying, so a damaged image fails loudly instead of
submitting silently. Running it twice
produces byte-identical output: a 1024×1024 PNG of about 172 KB, inside
the competition's 1 MiB and 1024×1024 limits.

## License

MIT — see [LICENSE](LICENSE).
