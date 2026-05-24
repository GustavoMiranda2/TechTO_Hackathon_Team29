import type { Roadmap } from "../types";

export default function RoadmapView({ data }: { data: Roadmap }) {
  return (
    <div className="card">
      <div className="section-title">Your 30-day study plan</div>
      <h3 style={{ marginBottom: 6 }}>{data.path_title}</h3>
      <a
        className="link"
        href={data.roadmap_url}
        target="_blank"
        rel="noreferrer"
      >
        Full study map on roadmap.sh →
      </a>

      <div className="skill-cols" style={{ marginTop: 20 }}>
        <div>
          <h4>Skip (you have it)</h4>
          {data.already_have.map((s) => (
            <span key={s} className="pill have">
              {s}
            </span>
          ))}
        </div>
        <div>
          <h4>Learn next</h4>
          {data.to_learn.map((s) => (
            <span key={s} className="pill missing">
              {s}
            </span>
          ))}
        </div>
      </div>

      <div style={{ marginTop: 20 }}>
        {data.weeks.map((w) => (
          <div key={w.week} className="week">
            <div className="wk">WEEK {w.week}</div>
            <div className="focus">{w.focus}</div>
            <ul>
              {w.tasks.map((t, i) => (
                <li key={i}>{t}</li>
              ))}
            </ul>
          </div>
        ))}
      </div>

      <div className="day" style={{ fontStyle: "normal" }}>
        <strong style={{ color: "var(--text)" }}>First project to build:</strong>{" "}
        {data.first_project}
      </div>
    </div>
  );
}
