import type { Diagnosis, InferredProfile, Match } from "../types";

function difficultyClass(d: string) {
  const v = d.toLowerCase();
  if (v.includes("reachable")) return "reachable";
  if (v.includes("aspirational")) return "aspirational";
  return "prep";
}

function splitList(value?: string) {
  return (value || "")
    .split(",")
    .map((item) => item.trim())
    .filter(Boolean)
    .slice(0, 8);
}

function SavedPreferences({
  profile,
  saved,
}: {
  profile?: InferredProfile;
  saved: boolean;
}) {
  if (!profile) return null;
  const groups = [
    ["Skills", splitList(profile.skills)],
    ["Interests", splitList(profile.interests)],
    ["Goals", profile.goals ? [profile.goals] : []],
    ["Career directions", splitList(profile.desired_roles)],
  ];

  return (
    <div className="saved-panel">
      <div>
        <p className="section-title">{saved ? "Saved for next time" : "Captured this session"}</p>
        <h3>Your preference snapshot</h3>
      </div>
      <div className="saved-grid">
        {groups.map(([label, values]) => (
          <div key={label as string} className="saved-group">
            <span>{label as string}</span>
            {(values as string[]).length > 0 ? (
              <div className="saved-tags">
                {(values as string[]).map((value) => (
                  <em key={value}>{value}</em>
                ))}
              </div>
            ) : (
              <p>Not enough signal yet.</p>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}

function MatchCard({
  match,
  selected,
  onSelect,
}: {
  match: Match;
  selected: boolean;
  onSelect: () => void;
}) {
  return (
    <button
      className={`card match ${selected ? "selected" : ""}`}
      onClick={onSelect}
    >
      <div className="match-head">
        <span className="title">{match.title}</span>
        <span className="score">{match.score}%</span>
      </div>
      <div className="bar">
        <div style={{ width: `${match.score}%` }} />
      </div>
      <span className={`tag ${difficultyClass(match.difficulty)}`}>
        {match.difficulty}
      </span>
      {match.role_overview && <p className="role-overview">{match.role_overview}</p>}
      <p className="why">{match.why}</p>
      {match.market_note && (
        <p className="market-note">
          <strong>Market note:</strong> {match.market_note}
        </p>
      )}
      <div className="skill-cols">
        <div>
          <h4>What points you here</h4>
          {match.have.map((s) => (
            <span key={s} className="pill have">
              {s}
            </span>
          ))}
        </div>
        <div>
          <h4>What you would grow into</h4>
          {match.missing.map((s) => (
            <span key={s} className="pill missing">
              {s}
            </span>
          ))}
        </div>
      </div>
      <div className="day">A Tuesday here: {match.day_in_life}</div>
    </button>
  );
}

export default function DiagnosisView({
  data,
  selectedKey,
  saved,
  onSelect,
}: {
  data: Diagnosis;
  selectedKey: string | null;
  saved: boolean;
  onSelect: (m: Match) => void;
}) {
  const m = data.misalignment;
  return (
    <div className="diagnosis-stack">
      <div className="result-hero">
        <p className="section-title">Career direction</p>
        <h2>{data.summary}</h2>
      </div>

      <SavedPreferences profile={data.inferred_profile} saved={saved} />

      {m.detected && (
        <div className="card misalign">
          <div className="section-title">Your past does not have to be your future</div>
          <div className="dirs">
            <div className="dir">
              <span>Your background leans</span>
              {m.background_points_to || "-"}
            </div>
            <div className="dir">
              <span>Your spark points to</span>
              {m.spark_points_to || "-"}
            </div>
          </div>
          <p className="why">{m.explanation}</p>
          <p>
            <strong>Where to explore next:</strong> {m.recommended_focus}
          </p>
        </div>
      )}

      <div className="section-row">
        <div>
          <p className="section-title">Your career compass</p>
          <h3>Pick a path to generate a roadmap</h3>
        </div>
        <span>{data.matches.length} matches</span>
      </div>
      <div className="match-grid">
        {data.matches.map((match) => (
          <MatchCard
            key={match.key}
            match={match}
            selected={selectedKey === match.key}
            onSelect={() => onSelect(match)}
          />
        ))}
      </div>
    </div>
  );
}
