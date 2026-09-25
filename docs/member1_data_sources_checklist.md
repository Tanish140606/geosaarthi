# GeoSaarthi — Member 1 (Data Engineer) — Day 1-2 Checklist

Goal for Day 1-2: don't download large datasets yet. Just confirm you
can **access** each source, and note the exact variables/files you'll
pull once the team has fixed the Assam study area.

## 1. ERA5 (your main climate dataset)

- Source: Copernicus Climate Data Store (CDS) — https://cds.climate.copernicus.eu
- [ ] Create a free account
- [ ] Go to your profile page and copy your **API key**
- [ ] Install the CDS API client: `pip install cdsapi` (or via conda)
- [ ] Create a file `.cdsapirc` in your home folder (C:\Users\<you>\.cdsapirc on
      Windows) with your URL + key as shown on your CDS profile page
- [ ] Test with a tiny request (e.g. 1 day, small bounding box) to confirm
      auth works — do NOT request a huge date range yet
- Variables to note down for later: total precipitation, 2m temperature,
  relative humidity, wind components, surface pressure

## 2. DEM (elevation)

- Source options: SRTM via USGS EarthExplorer (earthexplorer.usgs.gov) or
  OpenTopography (opentopography.org) — OpenTopography is usually easier
  for a quick download, no approval wait
- [ ] Create an account on whichever you pick
- [ ] Locate the tile(s) covering your team's chosen Assam study area
- [ ] Confirm you can download a small sample tile (don't need the full
      dataset yet)

## 3. Historical flood data

- Look for: ASDMA (Assam State Disaster Management Authority) reports,
  news archives around known flood years (e.g. 2019, 2020, 2022),
  and check if NASA's Global Flood Database or Dartmouth Flood
  Observatory has coverage for Assam
- [ ] Compile a simple table: Year | Approx. affected districts |
      Approx. rainfall (if reported) | Source link
- This becomes the seed for the Historical Analog Engine later —
  it doesn't need to be exhaustive, 5-8 well-documented events is enough
  for a prototype

## 4. Population data

- Source options: WorldPop (worldpop.org) or Census of India district-level
  data
- [ ] Confirm you can access/download gridded or district-level
      population figures for your study area

## 5. Shelters

- This one you can partly build yourself for the prototype: a small CSV
  with columns `shelter_id, name, lat, lon, capacity` for ~10-20 real or
  plausible locations (schools, community centers) in your study
  districts is enough to start
- [ ] Draft this CSV — even placeholder entries are fine for now, refine
      later if time allows

## What NOT to do yet

- Don't bulk-download full-resolution ERA5 for all of Assam for years of
  history — start with a small time/space slice once access is confirmed
- Don't wait for every dataset to be "perfect" before handing something
  to Member 2 — a small clean sample unblocks their work sooner

## Deliverable by end of Day 2

A short note to the team (Slack/Discord/doc) confirming: "I can access
X, Y, Z. Here's the exact variable list and date range I'll pull once
we lock the study area." That's it — real downloading starts Day 3.