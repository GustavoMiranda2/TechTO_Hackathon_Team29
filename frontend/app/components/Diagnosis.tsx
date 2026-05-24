import type { Diagnosis, Match } from "../types";

function difficultyClass(d: string) {
  const v = d.toLowerCase();
  if (v.includes("reachable")) return "reachable";
  if (v.includes("aspirational")) return "aspirational";
  return "prep";
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
    <div
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
      <p className="why">{match.why}</p>
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
          <h4>What you&apos;d grow into</h4>
          {match.missing.map((s) => (
            <span key={s} className="pill missing">
              {s}
            </span>
          ))}
        </div>
      </div>
      <div className="day">A Tuesday here: {match.day_in_life}</div>
    </div>
  );
}

export default function DiagnosisView({
  data,
  selectedKey,
  onSelect,
}: {
  data: Diagnosis;
  selectedKey: string | null;
  onSelect: (m: Match) => void;
}) {
  const m = data.misalignment;
  return (
    <div>
      <p className="summary">{data.summary}</p>

      {m.detected && (
        <div className="card misalign">
          <div className="section-title">Your past doesn&apos;t have to be your future</div>
          <div className="dirs">
            <div className="dir">
              <span>Your background leans</span>
              {m.background_points_to || "—"}
            </div>
            <div className="dir">
              <span>Your spark points to</span>
              {m.spark_points_to || "—"}
            </div>
          </div>
          <p className="why">{m.explanation}</p>
          <p>
            <strong>Where to explore next:</strong> {m.recommended_focus}
          </p>
        </div>
      )}

      <div className="section-title">Your career compass</div>
      {data.matches.map((match) => (
        <MatchCard
          key={match.key}
          match={match}
          selected={selectedKey === match.key}
          onSelect={() => onSelect(match)}
        />
      ))}
    </div>
  );
}
